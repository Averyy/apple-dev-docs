# type

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the session is a primary session or a mirrored session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var type: HKWorkoutSessionType { get }
```

```objc
@property (readonly) HKWorkoutSessionType type;
```

## See Also

### Accessing session data
- [var endDate: Date?](./enddate.md)
  The ending time and date for this workout session.
- [var startDate: Date?](./startdate.md)
  The starting time and date for this workout session.
- [var state: HKWorkoutSessionState](./state.md)
  The workout session’s current state.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration object that describes this workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/type)*