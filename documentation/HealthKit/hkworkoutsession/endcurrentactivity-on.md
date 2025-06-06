# endCurrentActivity(on:)

**Framework**: HealthKit  
**Kind**: method

Ends the current workout activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func endCurrentActivity(on date: Date)
```

## Mentions

- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)

#### Discussion

This method asynchronously ends the current activity. HealthKit calls the session delegate’s [`workoutSession(_:didEndActivityWith:date:)`](hkworkoutsessiondelegate/workoutsession(_:didendactivitywith:date:).md) method after the activity ends. HealthKit stops collecting data related to this activity.

## Parameters

- `date`: The end date and time for the activity.

## See Also

- [var currentActivity: HKWorkoutActivity](hkworkoutsession/currentactivity.md)
  The current workout activity.
- [func beginNewActivity(configuration: HKWorkoutConfiguration, date: Date, metadata: [String : Any]?)](hkworkoutsession/beginnewactivity(configuration:date:metadata:).md)
  Begins a new workout activity in the workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/endcurrentactivity(on:))*