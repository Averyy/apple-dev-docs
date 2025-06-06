# Providing Live Status Updates

**Framework**: SiriKit

Provide regular updates to Maps about the status of a booked ride.

#### Overview

After the user books a ride, Maps may call the [`startSendingUpdates(for:to:)`](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/startsendingupdates(for:to:)) method of your [`INGetRideStatusIntentHandling`](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling) handler object to ask for live status updates. Maps calls this method only once. Your implementation must set up a timer or other repeating task to generate status updates for the ride and deliver them to the provided observer object. Maps uses your updates to keep the user informed about the ride’s location and estimated arrival time.

The listing below shows a skeletal implementation of the [`startSendingUpdates(for:to:)`](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/startsendingupdates(for:to:)) method that sets up a timer for generating status updates. Because the system can call this method may on any thread, the implementation sets up the timer on the main thread, which ensures that the timer continues to fire.

```swift
public func startSendingUpdates(forGetRideStatus intent: INGetRideStatusIntent, 
            to observer: INGetRideStatusIntentResponseObserver) {
   // Save a reference to the observer object
   self.observer = observer
   // Set up the timer on the main thread and save a reference to it.
   DispatchQueue.main.async {
      self.timer = Timer.scheduledTimer(withTimeInterval: 5, 
                      repeats: true, block: { (timer) in
         let rideStatus = INRideStatus()
         // FOR YOU TO DO: Configure the INRideStatus object.

         // Create the response and deliver it.
         let response = INGetRideStatusIntentResponse(code: .success, userActivity: nil)
         response.rideStatus = rideStatus
         self.observer?.didUpdate(getRideStatus: response)
      })
   }
} 
```

When crafting your response, always include a valid [`INRideStatus`](https://developer.apple.com/documentation/intents/inridestatus) object. Here are some tips for configuring the status object to ensure that SiriKit processes your updates successfully:

-  Maps uses the [`phase`](https://developer.apple.com/documentation/intents/inridestatus/phase) property of the [`INRideStatus`](https://developer.apple.com/documentation/intents/inridestatus) object to communicate the ride status to the user. Specifically, when the phase changes, Maps updates that information in its interface. Never set the ride phase to [`INRidePhase.unknown`](https://developer.apple.com/documentation/intents/inridephase/unknown).
-  When setting the ride phase to [`INRidePhase.completed`](https://developer.apple.com/documentation/intents/inridephase/completed), assign an appropriate value to the [`completionStatus`](https://developer.apple.com/documentation/intents/inridestatus/completionstatus) property of the [`INRideStatus`](https://developer.apple.com/documentation/intents/inridestatus) object to indicate how to resolve the ride.
-  Updates must include the same value in the [`rideIdentifier`](https://developer.apple.com/documentation/intents/inridestatus/rideidentifier) property of the [`INRideStatus`](https://developer.apple.com/documentation/intents/inridestatus) object that you used when booking the ride. If the identifiers do not match, SiriKit ignores any further updates.
-  The value in the [`rideOption`](https://developer.apple.com/documentation/intents/inridestatus/rideoption) property of the [`INRideStatus`](https://developer.apple.com/documentation/intents/inridestatus) object need not match the one you specified during booking, but the ride option name and estimated pickup date must be valid.
-  Maps uses the map annotation image from your status object to show the position of your vehicle on the map surface. Specify this image using the [`mapAnnotationImage`](https://developer.apple.com/documentation/intents/inridevehicle/mapannotationimage) property of the [`INRideVehicle`](https://developer.apple.com/documentation/intents/inridevehicle) object you assign to your status object.

Upon the completion of a ride, call your handler object’s [`stopSendingUpdates(for:)`](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/stopsendingupdates(for:)) method when you want to stop the delivery of live updates. You implement this method and use it to cancel the recurring task that you use to generates updates. You can stop updates at any time, but typically you do so after the ride is complete and have settled any charges.

The listing below shows an implementation of the [`stopSendingUpdates(for:)`](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/stopsendingupdates(for:)) method that invalidates the timer used to deliver live updates and removes references to the observer object. Because both your code and SiriKit can call this method, it is an ideal place to perform all cleanup associated with live updates.

```swift
public func stopSendingUpdates(forGetRideStatus intent: INGetRideStatusIntent) {
   self.observer = nil
   self.timer?.invalidate()
	// Clean up any other state information.
}
```

The code you use to generate live updates must be fault-tolerant and able to handle errors well. Because getting live updates involves communicating with your server, you should handle cases where your server does not respond or returns an error. For example, you might return a cached response if your server does not respond in a timely manner. If you deliver an invalid response object to the observer, Maps calls the [`stopSendingUpdates(for:)`](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/stopsendingupdates(for:)) of your handler object and notifies the user that a problem occurred.

## See Also

- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Deleting Donated Shortcuts](deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Dispatching intents to handlers](dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving Siri Media Interactions and App Selection](improving-siri-media-interactions-and-app-selection.md)
  Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
- [Improving interactions between Siri and your messaging app](improving-interactions-between-siri-and-your-messaging-app.md)
  Donate app-specific content, use Siri’s contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
- [Registering Custom Vocabulary with SiriKit](registering-custom-vocabulary-with-sirikit.md)
  Register your app’s custom terminology, and provide sample phrases for how to use your app with Siri.
- [Confirming the Details of an Intent](confirming-the-details-of-an-intent.md)
  Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](handling-an-intent.md)
  Fulfill the intent and provide feedback to SiriKit about what you did.
- [Resolving the Parameters of an Intent](resolving-the-parameters-of-an-intent.md)
  Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Generating a List of Ride Options](generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [Handling the Ride-Booking Intents](handling-the-ride-booking-intents.md)
  Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Displaying Shortcut Information in a Siri Watch Face Card](displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/providing-live-status-updates)*