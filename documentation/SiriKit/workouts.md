# Workouts

**Framework**: SiriKit  
**Role**: API Collection

Start, end, and manage fitness routines.

#### Overview

Users can start, pause, resume, cancel, or end workouts with Siri. Your Intents app extension directs any workout-related requests to your app, which manages the actual workouts. SiriKit automatically asks users to unlock their device, as needed, before launching your app.

You can use an Intents UI app extension to provide a custom interface for workout-related intents.

![A screenshot of an Apple watch with Siri active and responding to the user’s request to start a running workout.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3743227@2x.png)

## Topics

### Essentials
- [Handling Workout Requests with SiriKit](./handling-workout-requests-with-sirikit.md)
  Add an Intent Extension to your app that handles requests to control workouts with Siri.
### Start a Workout
- [protocol INStartWorkoutIntentHandling](https://developer.apple.com/documentation/intents/instartworkoutintenthandling)
  An interface that handles requests to start a workout.
- [class INStartWorkoutIntent](https://developer.apple.com/documentation/intents/instartworkoutintent)
  A request to start a workout for the user.
- [class INStartWorkoutIntentResponse](https://developer.apple.com/documentation/intents/instartworkoutintentresponse)
  Your app’s response to a start workout intent.
### Pause a Workout
- [protocol INPauseWorkoutIntentHandling](https://developer.apple.com/documentation/intents/inpauseworkoutintenthandling)
  An interface that handles requests to pause a workout.
- [class INPauseWorkoutIntent](https://developer.apple.com/documentation/intents/inpauseworkoutintent)
  A request to pause the current workout that also stops the gathering of workout data.
- [class INPauseWorkoutIntentResponse](https://developer.apple.com/documentation/intents/inpauseworkoutintentresponse)
  Your app’s response to a pause workout intent.
### Resume a Workout
- [protocol INResumeWorkoutIntentHandling](https://developer.apple.com/documentation/intents/inresumeworkoutintenthandling)
  The interface that handles requests to resume a workout.
- [class INResumeWorkoutIntent](https://developer.apple.com/documentation/intents/inresumeworkoutintent)
  A request to resume a paused workout.
- [class INResumeWorkoutIntentResponse](https://developer.apple.com/documentation/intents/inresumeworkoutintentresponse)
  Your app’s response to a resume workout intent.
### Cancel a Workout
- [protocol INCancelWorkoutIntentHandling](https://developer.apple.com/documentation/intents/incancelworkoutintenthandling)
  The interface that handles requests to cancel a workout.
- [class INCancelWorkoutIntent](https://developer.apple.com/documentation/intents/incancelworkoutintent)
  A request to cancel an active workout.
- [class INCancelWorkoutIntentResponse](https://developer.apple.com/documentation/intents/incancelworkoutintentresponse)
  Your app’s response to a cancel workout intent.
### End a Workout
- [protocol INEndWorkoutIntentHandling](https://developer.apple.com/documentation/intents/inendworkoutintenthandling)
  An interface that handles requests to complete a workout.
- [class INEndWorkoutIntent](https://developer.apple.com/documentation/intents/inendworkoutintent)
  A request to end the current workout that also validates workout parameters and saves the results.
- [class INEndWorkoutIntentResponse](https://developer.apple.com/documentation/intents/inendworkoutintentresponse)
  Your app’s response to an end workout intent.
### Workout Data Objects
- [struct INWorkoutNameIdentifier](https://developer.apple.com/documentation/intents/inworkoutnameidentifier)
  Constants that indicate the type of workout.
- [enum INWorkoutGoalUnitType](https://developer.apple.com/documentation/intents/inworkoutgoalunittype)
  Describes the unit of measure with constants for a workout.
- [enum INWorkoutLocationType](https://developer.apple.com/documentation/intents/inworkoutlocationtype)
  Describes the location of a workout.
### Resolution Results
- [class INWorkoutGoalUnitTypeResolutionResult](https://developer.apple.com/documentation/intents/inworkoutgoalunittyperesolutionresult)
  A resolution result for the units of a workout goal.
- [class INWorkoutLocationTypeResolutionResult](https://developer.apple.com/documentation/intents/inworkoutlocationtyperesolutionresult)
  A resolution result for the location type where the workout occurs.

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
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/workouts)*