# endCurrentActivity(on:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Ends the current workout activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func endCurrentActivity(on date: Date)
```

```objc
- (void) endCurrentActivityOnDate:(NSDate *) date;
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

#### Discussion

This method asynchronously ends the current activity. HealthKit calls the session delegate’s [`workoutSession(_:didEndActivityWith:date:)`](../hkworkoutsessiondelegate/workoutsession%28_,didendactivitywith,date%29.md) method after the activity ends. HealthKit stops collecting data related to this activity.

## Parameters

- `date`: The end date and time for the activity.

## See Also

### Managing workout activities
- [var currentActivity: HKWorkoutActivity](./currentactivity.md)
  The current workout activity.
- [func beginNewActivity(configuration: HKWorkoutConfiguration, date: Date, metadata: [String : Any]?)](./beginnewactivity%28configuration,date,metadata%29.md)
  Begins a new workout activity in the workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/endcurrentactivity(on:))*