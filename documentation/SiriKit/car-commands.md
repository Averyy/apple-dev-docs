# Car Commands

**Framework**: SiriKit  
**Role**: API Collection

Manage vehicle door locks and get the vehicle’s status.

## Overview

Users can lock or unlock the car’s doors and get other car-related information using Siri. Automotive vendors use their Intents app extension to validate the user’s request and communicate with the user’s registered vehicles.

## Topics

### Get Car Lock Status
- [protocol INGetCarLockStatusIntentHandling](../Intents/ingetcarlockstatusintenthandling.md)
  The handler interface for requesting the current status of the car’s locks.
- [class INGetCarLockStatusIntent](../Intents/ingetcarlockstatusintent.md)
  A request to get the lock status of the user’s car.
- [class INGetCarLockStatusIntentResponse](../Intents/ingetcarlockstatusintentresponse.md)
  Your app’s response to a request to get the car’s lock status.
### Set Car Lock Status
- [protocol INSetCarLockStatusIntentHandling](../Intents/insetcarlockstatusintenthandling.md)
  The handler interface for requesting to lock or unlock a car.
- [class INSetCarLockStatusIntent](../Intents/insetcarlockstatusintent.md)
  A request to lock or unlock the user’s car.
- [class INSetCarLockStatusIntentResponse](../Intents/insetcarlockstatusintentresponse.md)
  Your app’s response to a request to lock or unlock the car.
### Get Car Power Level Status
- [protocol INGetCarPowerLevelStatusIntentHandling](../Intents/ingetcarpowerlevelstatusintenthandling.md)
  The handler interface for requesting a car’s current power level.
- [class INGetCarPowerLevelStatusIntent](../Intents/ingetcarpowerlevelstatusintent.md)
  A request for the current power level of the user’s car.
- [class INGetCarPowerLevelStatusIntentResponse](../Intents/ingetcarpowerlevelstatusintentresponse.md)
  Your app’s response to a request for the vehicle power level.
- [protocol INGetCarPowerLevelStatusIntentResponseObserver](../Intents/ingetcarpowerlevelstatusintentresponseobserver.md)
  The interface for providing updates of a vehicle’s power level.
### Activate Car Signal
- [protocol INActivateCarSignalIntentHandling](../Intents/inactivatecarsignalintenthandling.md)
  The handler interface for requesting to activate the car’s signals.
- [class INActivateCarSignalIntent](../Intents/inactivatecarsignalintent.md)
  A request to activate the signals on the user’s car.
- [class INActivateCarSignalIntentResponse](../Intents/inactivatecarsignalintentresponse.md)
  Your app’s response to a request to activate a car’s signals.
### List Cars
- [protocol INListCarsIntentHandling](../Intents/inlistcarsintenthandling.md)
  The handler interface for requesting a list of the user’s electric vehicles.
- [class INListCarsIntent](../Intents/inlistcarsintent.md)
  An intent for retrieving a list of the user’s electric vehicles.
- [class INListCarsIntentResponse](../Intents/inlistcarsintentresponse.md)
  Your app’s response to a request to list the user’s electric vehicles.
### Data Objects
- [struct INCarSignalOptions](../Intents/incarsignaloptions.md)
  The signals produced by the user’s car.
### Resolution Results
- [class INCarSignalOptionsResolutionResult](../Intents/incarsignaloptionsresolutionresult.md)
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