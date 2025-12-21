# Workouts and activity rings

**Framework**: HealthKit

Manage workouts, workout sessions, and activity summaries.

#### Overview

A workout is a sample that contains data about an exercise or fitness activity. You save workout data using the [`HKWorkout`](hkworkout.md) class. In many ways, workouts are identical to any other HealthKit sample—the same advice and APIs apply to both workouts and samples. However, workouts do have a number of unique features, described in [`HKWorkout`](hkworkout.md).

Workout sessions let you track the user’s activity on Apple Watch. While  a workout session is active, your app can continue to run in the background. This lets your app monitor the user and gather data throughout the activity. Additionally, it ensures that your app appears whenever the user checks their watch. After the session ends, your app saves the activity’s data as a workout sample. For more information on setting up and running workout sessions, see [`HKWorkoutSession`](hkworkoutsession.md).

The Activity Rings display a summary of the user’s daily activity on Apple Watch and in the Activity app. Activity summaries provide access to the data displayed in the user’s Move, Exercise, and Stand rings. To see how your workout samples contribute to these rings, see [`Fill the Activity rings`](hkworkout#Fill-the-Activity-rings.md). To learn more about accessing and displaying activity data in your app, see Activity rings.

Finally, workout routes record the user’s path during an outdoor activity (for example, while walking, running, or cycling). Routes can be associated with a workout sample. For more information, see [`Creating a workout route`](creating-a-workout-route.md) and [`Reading route data`](reading-route-data.md).

## Topics

### Samples
- [Adding samples to a workout](adding-samples-to-a-workout.md)
  Create associated samples that add details to a workout.
- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)
  Read series data from condensed workouts.
- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)
  Partition multisport and interval workouts into activities that represent the different parts of the workout.
- [class HKWorkout](hkworkout.md)
  A workout sample that stores information about a single physical activity.
- [class HKWorkoutActivity](hkworkoutactivity.md)
  An object that describes an activity within a longer workout.
- [class HKWorkoutBuilder](hkworkoutbuilder.md)
  A builder object that incrementally constructs a workout.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [let HKWorkoutTypeIdentifier: String](hkworkouttypeidentifier.md)
  The workout type identifier.
- [enum HKWorkoutActivityType](hkworkoutactivitytype.md)
  The type of activity performed during a workout.
- [enum HKWorkoutSessionType](hkworkoutsessiontype.md)
  The type of session.
- [class HKWorkoutEvent](hkworkoutevent.md)
  An object representing an important event during a workout.
### Sessions
- [Running workout sessions](running-workout-sessions.md)
  Track a workout on Apple Watch.
- [Build a workout app for Apple Watch](build-a-workout-app-for-apple-watch.md)
  Create your own workout app, quickly and easily, with HealthKit and SwiftUI.
- [Building a multidevice workout app](building-a-multidevice-workout-app.md)
  Mirror a workout from a watchOS app to its companion iOS app, and perform bidirectional communication between them.
- [Building a workout app for iPhone and iPad](building-a-workout-app-for-iphone-and-ipad.md)
  Start a workout in iOS, control it from the Lock Screen with App Intents, and present the workout status with Live Activities.
- [class HKWorkoutSession](hkworkoutsession.md)
  A session that tracks a person’s workout.
- [class HKWorkoutConfiguration](hkworkoutconfiguration.md)
  An object that contains configuration information about a workout session.
- [enum HKWorkoutSessionState](hkworkoutsessionstate.md)
  A workout session’s state.
- [class HKLiveWorkoutBuilder](hkliveworkoutbuilder.md)
  A builder object that constructs a workout incrementally based on live data from an active workout session.
- [class HKLiveWorkoutDataSource](hkliveworkoutdatasource.md)
  A data source that automatically provides live data from an active workout session.
### Activity rings
- [class HKActivitySummary](hkactivitysummary.md)
  An object that contains the move, exercise, and stand data for a given day.
- [struct HKActivitySummaryQueryDescriptor](hkactivitysummaryquerydescriptor.md)
  A query interface that reads activity summaries using Swift concurrency.
- [class HKActivitySummaryQuery](hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [class HKActivityRingView](../healthkitui/hkactivityringview.md)
  A view that uses the Move, Exercise, and Stand activity rings to display data from a HealthKit activity summary object.
- [class HKActivityMoveModeObject](hkactivitymovemodeobject.md)
  An object that contains a movement mode value.
### Route data
- [Creating a workout route](creating-a-workout-route.md)
  Record the user’s route during a workout.
- [Reading route data](reading-route-data.md)
  Access the user’s route for a workout.
- [class HKWorkoutRouteBuilder](hkworkoutroutebuilder.md)
  A builder object that incrementally constructs a workout route.
- [class HKWorkoutRoute](hkworkoutroute.md)
  A sample that contains a workout’s route data.
- [struct HKWorkoutRouteQueryDescriptor](hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [class HKWorkoutRouteQuery](hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [let HKWorkoutRouteTypeIdentifier: String](hkworkoutroutetypeidentifier.md)
  A series sample containing location data that defines the route the user took during a workout.
- [class HKSeriesBuilder](hkseriesbuilder.md)
  An abstract base class for building series samples.
- [class HKSeriesSample](hkseriessample.md)
  An abstract base class that defines samples that contain a series of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings)*