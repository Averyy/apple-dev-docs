# Car Commands

**Framework**: SiriKit  
**Role**: API Collection

Manage vehicle door locks and get the vehicle’s status.

#### Overview

Users can lock or unlock the car’s doors and get other car-related information using Siri. Automotive vendors use their Intents app extension to validate the user’s request and communicate with the user’s registered vehicles.

## Topics

### Get Car Lock Status
- [protocol INGetCarLockStatusIntentHandling](https://developer.apple.com/documentation/intents/ingetcarlockstatusintenthandling)
  The handler interface for requesting the current status of the car’s locks.
- [class INGetCarLockStatusIntent](https://developer.apple.com/documentation/intents/ingetcarlockstatusintent)
  A request to get the lock status of the user’s car.
- [class INGetCarLockStatusIntentResponse](https://developer.apple.com/documentation/intents/ingetcarlockstatusintentresponse)
  Your app’s response to a request to get the car’s lock status.
### Set Car Lock Status
- [protocol INSetCarLockStatusIntentHandling](https://developer.apple.com/documentation/intents/insetcarlockstatusintenthandling)
  The handler interface for requesting to lock or unlock a car.
- [class INSetCarLockStatusIntent](https://developer.apple.com/documentation/intents/insetcarlockstatusintent)
  A request to lock or unlock the user’s car.
- [class INSetCarLockStatusIntentResponse](https://developer.apple.com/documentation/intents/insetcarlockstatusintentresponse)
  Your app’s response to a request to lock or unlock the car.
### Get Car Power Level Status
- [protocol INGetCarPowerLevelStatusIntentHandling](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintenthandling)
  The handler interface for requesting a car’s current power level.
- [class INGetCarPowerLevelStatusIntent](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintent)
  A request for the current power level of the user’s car.
- [class INGetCarPowerLevelStatusIntentResponse](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse)
  Your app’s response to a request for the vehicle power level.
- [protocol INGetCarPowerLevelStatusIntentResponseObserver](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponseobserver)
  The interface for providing updates of a vehicle’s power level.
### Activate Car Signal
- [protocol INActivateCarSignalIntentHandling](https://developer.apple.com/documentation/intents/inactivatecarsignalintenthandling)
  The handler interface for requesting to activate the car’s signals.
- [class INActivateCarSignalIntent](https://developer.apple.com/documentation/intents/inactivatecarsignalintent)
  A request to activate the signals on the user’s car.
- [class INActivateCarSignalIntentResponse](https://developer.apple.com/documentation/intents/inactivatecarsignalintentresponse)
  Your app’s response to a request to activate a car’s signals.
### List Cars
- [protocol INListCarsIntentHandling](https://developer.apple.com/documentation/intents/inlistcarsintenthandling)
  The handler interface for requesting a list of the user’s electric vehicles.
- [class INListCarsIntent](https://developer.apple.com/documentation/intents/inlistcarsintent)
  An intent for retrieving a list of the user’s electric vehicles.
- [class INListCarsIntentResponse](https://developer.apple.com/documentation/intents/inlistcarsintentresponse)
  Your app’s response to a request to list the user’s electric vehicles.
### Data Objects
- [struct INCarSignalOptions](https://developer.apple.com/documentation/intents/incarsignaloptions)
  The signals produced by the user’s car.
### Resolution Results
- [class INCarSignalOptionsResolutionResult](https://developer.apple.com/documentation/intents/incarsignaloptionsresolutionresult)
  A resolution result for the signals the intent is managing on the car.

## See Also

### Standard Intents
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
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/car-commands)*