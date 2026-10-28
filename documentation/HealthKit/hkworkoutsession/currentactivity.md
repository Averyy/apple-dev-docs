# currentActivity

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The current workout activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var currentActivity: HKWorkoutActivity { get }
```

```objc
@property (copy, readonly) HKWorkoutActivity * currentActivity;
```

## Discussion

This property contains a workout activity that’s currently in progress (an activity with an [`endDate`](../hkworkoutactivity/enddate.md) property set to `nil`). If you end the activity — for example, by calling [`endCurrentActivity(on:)`](./endcurrentactivity%28on%29.md) or [`updateActivity(uuid:end:completion:)`](../hkworkoutbuilder/updateactivity%28uuid,end,completion%29.md) — the system sets this property to `nil` until you begin a new activity.

## See Also

### Managing workout activities
- [func beginNewActivity(configuration: HKWorkoutConfiguration, date: Date, metadata: [String : Any]?)](./beginnewactivity%28configuration,date,metadata%29.md)
  Begins a new workout activity in the workout session.
- [func endCurrentActivity(on: Date)](./endcurrentactivity%28on%29.md)
  Ends the current workout activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/currentactivity)*