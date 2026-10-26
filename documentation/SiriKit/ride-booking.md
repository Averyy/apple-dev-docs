# Ride Booking

**Framework**: SiriKit  
**Role**: API Collection

Book rides and report their status.

#### Overview

Users can book rides from Maps, Shortcuts, and Siri Suggestions. When the user requests a ride from your service, SiriKit forwards the information to your Intents app extension for processing. The user can ask you to provide a list of available rides, to initiate the booking of a ride, and to provide status updates for a booked ride. Maps expects you to handle all of the intents in this domain and won’t load your Intents app extension if you don’t support all of them.

You can provide a custom interface for ride-booking intents using an Intents UI app extension.

> ❗ **Important**:  For information about Siri and Ride Booking, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Topics

### Essentials
- [Handling the Ride-Booking Intents](./handling-the-ride-booking-intents.md)
  Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Booking Rides with SiriKit](./booking-rides-with-sirikit.md)
  Add Intents extensions to your app to handle requests to book rides using Siri and Maps.
### List Ride Options
- [Generating a List of Ride Options](./generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [protocol INListRideOptionsIntentHandling](https://developer.apple.com/documentation/intents/inlistrideoptionsintenthandling)
  The handler interface for fetching the list of rides currently available from your ride-booking service.
- [class INListRideOptionsIntent](https://developer.apple.com/documentation/intents/inlistrideoptionsintent)
  An intent for getting the types of rides available from a ride-booking service.
- [class INListRideOptionsIntentResponse](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponse)
  Your app’s response to a list ride options intent.
### Request a Ride
- [protocol INRequestRideIntentHandling](https://developer.apple.com/documentation/intents/inrequestrideintenthandling)
  The handler interface for booking a ride for the user.
- [class INRequestRideIntent](https://developer.apple.com/documentation/intents/inrequestrideintent)
  A request to book the specified ride from your service.
- [class INRequestRideIntentResponse](https://developer.apple.com/documentation/intents/inrequestrideintentresponse)
  Your app’s response to a request ride intent.
### Get the Ride Status
- [protocol INGetRideStatusIntentHandling](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling)
  The handler interface for fetching the status of the user’s current ride.
- [class INGetRideStatusIntent](https://developer.apple.com/documentation/intents/ingetridestatusintent)
  A request for the current status of a previously booked ride.
- [class INGetRideStatusIntentResponse](https://developer.apple.com/documentation/intents/ingetridestatusintentresponse)
  Your app’s response to a get ride status intent.
- [protocol INGetRideStatusIntentResponseObserver](https://developer.apple.com/documentation/intents/ingetridestatusintentresponseobserver)
  An interface for providing updated status for an active ride.
### Cancel Ride
- [protocol INCancelRideIntentHandling](https://developer.apple.com/documentation/intents/incancelrideintenthandling)
  The handler interface for canceling a previously booked ride.
- [class INCancelRideIntent](https://developer.apple.com/documentation/intents/incancelrideintent)
  An intent requesting the cancellation of a previously booked ride.
- [class INCancelRideIntentResponse](https://developer.apple.com/documentation/intents/incancelrideintentresponse)
  Your app’s response to a cancel ride intent.
### Send Ride Feedback
- [protocol INSendRideFeedbackIntentHandling](https://developer.apple.com/documentation/intents/insendridefeedbackintenthandling)
  The handler interface for sending ride feedback to your service.
- [class INSendRideFeedbackIntent](https://developer.apple.com/documentation/intents/insendridefeedbackintent)
  An intent indicating that the user provided feedback for a completed ride.
- [class INSendRideFeedbackIntentResponse](https://developer.apple.com/documentation/intents/insendridefeedbackintentresponse)
  Your app’s response to a send ride feedback intent.
### Data Objects
- [class INRideOption](https://developer.apple.com/documentation/intents/inrideoption)
  Details about a type of ride offered by your ride-booking service.
- [class INRideStatus](https://developer.apple.com/documentation/intents/inridestatus)
  The status of a ride booked through a ride-booking service.
- [class INRideDriver](https://developer.apple.com/documentation/intents/inridedriver)
  Identifying information about a driver of a ride service.
- [class INRideVehicle](https://developer.apple.com/documentation/intents/inridevehicle)
  A specific vehicle used by a ride-booking service.
- [class INRideFareLineItem](https://developer.apple.com/documentation/intents/inridefarelineitem)
  A specific type of ride-related charge.
- [class INRidePartySizeOption](https://developer.apple.com/documentation/intents/inridepartysizeoption)
  The price of a ride involving the specified number of people.
- [class INRideCompletionStatus](https://developer.apple.com/documentation/intents/inridecompletionstatus)
  Additional details about whether a ride completed successfully or someone canceled the ride.

## See Also

### Standard Intents
- [Car Commands](./car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Lists and Notes](./lists-and-notes.md)
  Create and manage notes and to-do list items.
- [Media](./media.md)
  Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.
- [Messaging](./messaging.md)
  Send messages and search the user’s received messages.
- [Payments](./payments.md)
  Send payments between users or pay bills.
- [Restaurant Reservations](./restaurant-reservations.md)
  Create and manage restaurant reservations with help from the Maps app.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/ride-booking)*