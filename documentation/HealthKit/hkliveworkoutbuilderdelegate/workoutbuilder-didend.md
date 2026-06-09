# workoutBuilder(_:didEnd:)

**Framework**: HealthKit  
**Kind**: method

Tells the delegate that the current workout activity has ended.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
optional func workoutBuilder(_ workoutBuilder: HKLiveWorkoutBuilder, didEnd workoutActivity: HKWorkoutActivity)
```

## Parameters

- `workoutBuilder`: The workout builder that received the new activity.
- `workoutActivity`: The workout activity that just ended.

## See Also

- [func workoutBuilder(HKLiveWorkoutBuilder, didBegin: HKWorkoutActivity)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didbegin:).md)
  Tells the delegate that a new workout activity has started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilder(_:didend:))*