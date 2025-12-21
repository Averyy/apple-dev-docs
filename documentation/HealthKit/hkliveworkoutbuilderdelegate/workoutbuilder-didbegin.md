# workoutBuilder(_:didBegin:)

**Framework**: HealthKit  
**Kind**: method

Tells the delegate that a new workout activity has started.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
optional func workoutBuilder(_ workoutBuilder: HKLiveWorkoutBuilder, didBegin workoutActivity: HKWorkoutActivity)
```

## Parameters

- `workoutBuilder`: The workout builder that received the new activity.
- `workoutActivity`: A new workout activity, currently in progress.

## See Also

- [func workoutBuilder(HKLiveWorkoutBuilder, didCollectDataOf: Set<HKSampleType>)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:).md)
  Tells the delegate that new data has been added to the builder.
- [func workoutBuilderDidCollectEvent(HKLiveWorkoutBuilder)](hkliveworkoutbuilderdelegate/workoutbuilderdidcollectevent(_:).md)
  Tells the delegate that a new event has been added to the builder.
- [func workoutBuilder(HKLiveWorkoutBuilder, didEnd: HKWorkoutActivity)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didend:).md)
  Tells the delegate that the current workout activity has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilder(_:didbegin:))*