# HKWorkoutSession

**Framework**: HealthKit  
**Kind**: class

A session that tracks the user’s workout on Apple Watch.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKWorkoutSession
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

#### Overview

The session fine-tunes Apple Watch’s sensors for the specified activity. All workout sessions generate high-frequency heart rate samples; however, an outdoor cycling activity generates accurate location data, while an indoor cycling activity doesn’t.

Apple Watch runs one workout session at a time. If a second workout starts while your workout is running, your [`HKWorkoutSessionDelegate`](hkworkoutsessiondelegate.md) object receives an [`HKError.Code.errorAnotherWorkoutSessionStarted`](hkerror/code/erroranotherworkoutsessionstarted.md) error, and your session ends.

## Topics

### Creating workout sessions
- [init(healthStore: HKHealthStore, configuration: HKWorkoutConfiguration) throws](hkworkoutsession/init(healthstore:configuration:).md)
  Returns a newly instantiated workout session with an associated workout builder.
### Monitoring the session
- [var delegate: (any HKWorkoutSessionDelegate)?](hkworkoutsession/delegate.md)
  The workout session’s delegate.
- [protocol HKWorkoutSessionDelegate](hkworkoutsessiondelegate.md)
  The session delegate protocol that defines an interface for receiving notifications about errors and changes in the workout session’s state.
### Accessing the workout builder
- [func associatedWorkoutBuilder() -> HKLiveWorkoutBuilder](hkworkoutsession/associatedworkoutbuilder.md)
  Returns the live workout builder associated with the workout session.
### Managing the workout
- [func prepare()](hkworkoutsession/prepare.md)
  Prepares the workout session.
- [func startActivity(with: Date?)](hkworkoutsession/startactivity(with:).md)
  Starts the workout session activity, and sets the start date.
- [func pause()](hkworkoutsession/pause.md)
  Pauses the workout session.
- [func resume()](hkworkoutsession/resume.md)
  Resumes the workout session.
- [func stopActivity(with: Date?)](hkworkoutsession/stopactivity(with:).md)
  Stops the workout session activity, and sets the end date.
- [func end()](hkworkoutsession/end.md)
  Ends the workout session.
### Working with remote workout sessions
- [func startMirroringToCompanionDevice(completion: (Bool, (any Error)?) -> Void)](hkworkoutsession/startmirroringtocompaniondevice(completion:).md)
  Starts mirroring the workout session to the companion iOS device.
- [func stopMirroringToCompanionDevice(completion: (Bool, (any Error)?) -> Void)](hkworkoutsession/stopmirroringtocompaniondevice(completion:).md)
  Stops mirroring the workout session to the companion iOS device.
- [func sendToRemoteWorkoutSession(data: Data, completion: (Bool, (any Error)?) -> Void)](hkworkoutsession/sendtoremoteworkoutsession(data:completion:).md)
  Sends the provided data to the remote workout session.
### Accessing session data
- [var endDate: Date?](hkworkoutsession/enddate.md)
  The ending time and date for this workout session.
- [var startDate: Date?](hkworkoutsession/startdate.md)
  The starting time and date for this workout session.
- [var state: HKWorkoutSessionState](hkworkoutsession/state.md)
  The workout session’s current state.
- [var type: HKWorkoutSessionType](hkworkoutsession/type.md)
  A value that indicates whether the session is a primary session or a mirrored session.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutsession/workoutconfiguration.md)
  The configuration object that describes this workout.
### Managing workout activities
- [var currentActivity: HKWorkoutActivity](hkworkoutsession/currentactivity.md)
  The current workout activity.
- [func beginNewActivity(configuration: HKWorkoutConfiguration, date: Date, metadata: [String : Any]?)](hkworkoutsession/beginnewactivity(configuration:date:metadata:).md)
  Begins a new workout activity in the workout session.
- [func endCurrentActivity(on: Date)](hkworkoutsession/endcurrentactivity(on:).md)
  Ends the current workout activity.
### Deprecated methods
- [init(activityType: HKWorkoutActivityType, locationType: HKWorkoutSessionLocationType)](hkworkoutsession/init(activitytype:locationtype:).md)
  Returns a newly instantiated workout session.
- [init(configuration: HKWorkoutConfiguration) throws](hkworkoutsession/init(configuration:).md)
  Returns a newly instantiated workout session.
- [var activityType: HKWorkoutActivityType](hkworkoutsession/activitytype.md)
  The workout activity performed during this session.
- [var locationType: HKWorkoutSessionLocationType](hkworkoutsession/locationtype.md)
  A value that indicates whether the workout session occurred indoors or outdoors.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Running workout sessions](running-workout-sessions.md)
  Track a workout on Apple Watch.
- [Build a workout app for Apple Watch](build-a-workout-app-for-apple-watch.md)
  Create your own workout app, quickly and easily, with HealthKit and SwiftUI.
- [Building a multidevice workout app](building-a-multidevice-workout-app.md)
  Mirror a workout from a watchOS app to its companion iOS app, and perform bidirectional communication between them.
- [Building a workout app for iPhone and iPad](building-a-workout-app-for-iphone-and-ipad.md)
  Start a workout in iOS, control it from the Lock Screen with App Intents, and present the workout status with Live Activities.
- [class HKWorkoutConfiguration](hkworkoutconfiguration.md)
  An object that contains configuration information about a workout session.
- [enum HKWorkoutSessionState](hkworkoutsessionstate.md)
  A workout session’s state.
- [class HKLiveWorkoutBuilder](hkliveworkoutbuilder.md)
  A builder object that constructs a workout incrementally based on live data from an active workout session.
- [class HKLiveWorkoutDataSource](hkliveworkoutdatasource.md)
  A data source that automatically provides live data from an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession)*