# workoutBuilder(_:didEnd:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) workoutBuilder:(HKLiveWorkoutBuilder *) workoutBuilder didEndActivity:(HKWorkoutActivity *) workoutActivity;
```

## Parameters

- `workoutBuilder`: The workout builder that received the new activity.
- `workoutActivity`: The workout activity that just ended.

## See Also

### Receiving activity updates
- [func workoutBuilder(HKLiveWorkoutBuilder, didBegin: HKWorkoutActivity)](./workoutbuilder%28_,didbegin%29.md)
  Tells the delegate that a new workout activity has started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilder(_:didend:))*