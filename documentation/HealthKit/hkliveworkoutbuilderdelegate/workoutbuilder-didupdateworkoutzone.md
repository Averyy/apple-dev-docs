# workoutBuilder(_:didUpdateWorkoutZone:)

**Framework**: HealthKit  
**Kind**: method

Tells the delegate that the person changed zones during the workout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS ?+
- watchOS 27.0+ (Beta)

## Declaration

```swift
optional func workoutBuilder(_ workoutBuilder: HKLiveWorkoutBuilder, didUpdateWorkoutZone zoneUpdate: HKLiveWorkoutZoneUpdate)
```

## Mentions

- [Accessing workout zone data](accessing-workout-zone-data.md)

#### Discussion

The system calls this method when the person moves between zones. Use this method to update your app’s interface to reflect the current zone or to provide feedback about zone changes.

## Parameters

- `workoutBuilder`: The live workout builder instance.
- `zoneUpdate`: Details about the zone transition and current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilder(_:didupdateworkoutzone:))*