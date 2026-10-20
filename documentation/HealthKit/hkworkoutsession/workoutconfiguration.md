# workoutConfiguration

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The configuration object that describes this workout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var workoutConfiguration: HKWorkoutConfiguration { get }
```

```objc
@property (copy, readonly) HKWorkoutConfiguration * workoutConfiguration;
```

#### Discussion

Returns a copy of the configuration object passed to [`init(configuration:)`](./init%28configuration%29.md) when instantiating the workout session. Changes made to the returned value have no affect on the workout session.

## See Also

### Accessing session data
- [var endDate: Date?](./enddate.md)
  The ending time and date for this workout session.
- [var startDate: Date?](./startdate.md)
  The starting time and date for this workout session.
- [var state: HKWorkoutSessionState](./state.md)
  The workout session’s current state.
- [var type: HKWorkoutSessionType](./type.md)
  A value that indicates whether the session is a primary session or a mirrored session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/workoutconfiguration)*