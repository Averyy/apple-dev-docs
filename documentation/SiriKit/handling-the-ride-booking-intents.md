# Handling the Ride-Booking Intents

**Framework**: Sirikit

Support the different intent-handling sequences for booking rides with Shortcuts or Maps.

#### Overview

A successful implementation of a ride-booking Intents app extension requires supporting all of the intents in the ride-booking domain. In fact, Maps on iOS expects your extension to handle all of the intents and doesn’t load it if it doesn’t.

A ride-booking Intents app extension provides a list of available vehicles, details about the cost of each ride, and status updates for any booked rides. It also facilitates financial transactions associated with any rides and communicates any relevant information to your ride booking service. Shortcuts and Maps handle ride booking differently, and your extension must be able to support both flows.

##### Book Rides From Maps

With Maps, users specify information such as the start and end points of their route directly using the Maps interface. Then Maps sends an [`INListRideOptionsIntent`](https://developer.apple.com/documentation/intents/inlistrideoptionsintent) object that describes the user’s trip to your Intents app extension. Provide ride options available for the user’s requested trip. For more information about providing effective ride options, see [`Generating a List of Ride Options`](generating-a-list-of-ride-options.md). After the user selects one of your ride options, Maps sends an [`INRequestRideIntent`](https://developer.apple.com/documentation/intents/inrequestrideintent) object to your Intents app extension to handle. Use the information in this object to book the ride.

> **Note**:  When you handle a ride-booking intent from Maps, there isn’t a resolve or confirm step. Instead, Maps validates the user’s origin and destination before sending intents to your Intents app extension.

Maps may send the same [`INGetRideStatusIntent`](https://developer.apple.com/documentation/intents/ingetridestatusintent) object to your Intents app extension multiple times after booking is complete. Maps may also call the [`startSendingUpdates(for:to:)`](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/startsendingupdates(for:to:)) method of your intent handler to ask for live status updates. Prepare your handler to push frequent status updates to the specified observer object. For information about how to handle live status updates, see [`Providing Live Status Updates`](providing-live-status-updates.md).

##### Book Rides From Shortcuts and Siri Suggestions

Shortcuts and Siri Suggestions send your Intents app extension [`INRequestRideIntent`](https://developer.apple.com/documentation/intents/inrequestrideintent) objects to resolve, confirm, and handle. For more details about this sequence, see doc://com.apple.documentation/documentation/sirikit/resolving_and_handling_intents. Implement the methods in the [`INRequestRideIntentHandling`](https://developer.apple.com/documentation/intents/inrequestrideintenthandling) protocol to prompt the user for additional information and confirm the details of their trip.

## Topics

### Related Articles
- [Generating a List of Ride Options](generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [Providing Live Status Updates](providing-live-status-updates.md)
  Provide regular updates to Maps about the status of a booked ride.

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
- [Displaying Shortcut Information in a Siri Watch Face Card](displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SiriKit/handling-the-ride-booking-intents)*