# currentActivity

**Framework**: HealthKit  
**Kind**: property

The current workout activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var currentActivity: HKWorkoutActivity { get }
```

#### Discussion

This property contains a workout activity that’s currently in progress (an activity with an [`endDate`](hkworkoutactivity/enddate.md) property set to `nil`). If you end the activity — for example, by calling [`endCurrentActivity(on:)`](hkworkoutsession/endcurrentactivity(on:).md) or [`updateActivity(uuid:end:completion:)`](hkworkoutbuilder/updateactivity(uuid:end:completion:).md) — the system sets this property to `nil` until you begin a new activity.

## See Also

- [func beginNewActivity(configuration: HKWorkoutConfiguration, date: Date, metadata: [String : Any]?)](hkworkoutsession/beginnewactivity(configuration:date:metadata:).md)
  Begins a new workout activity in the workout session.
- [func endCurrentActivity(on: Date)](hkworkoutsession/endcurrentactivity(on:).md)
  Ends the current workout activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/currentactivity)*