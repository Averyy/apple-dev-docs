# workoutBuilder(_:didEnd:)

**Framework**: HealthKit  
**Kind**: method

Tells the delegate that the current workout activity has ended.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
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

- [func workoutBuilder(HKLiveWorkoutBuilder, didCollectDataOf: Set<HKSampleType>)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:).md)
  Tells the delegate that new data has been added to the builder.
- [func workoutBuilderDidCollectEvent(HKLiveWorkoutBuilder)](hkliveworkoutbuilderdelegate/workoutbuilderdidcollectevent(_:).md)
  Tells the delegate that a new event has been added to the builder.
- [func workoutBuilder(HKLiveWorkoutBuilder, didBegin: HKWorkoutActivity)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didbegin:).md)
  Tells the delegate that a new workout activity has started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilder(_:didend:))*