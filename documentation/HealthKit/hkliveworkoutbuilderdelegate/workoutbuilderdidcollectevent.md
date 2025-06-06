# workoutBuilderDidCollectEvent(_:)

**Framework**: HealthKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that a new event has been added to the builder.

**Availability**:
- macOS ?+
- watchOS 5.0+

## Declaration

```swift
func workoutBuilderDidCollectEvent(_ workoutBuilder: HKLiveWorkoutBuilder)
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

## See Also

- [func workoutBuilder(HKLiveWorkoutBuilder, didCollectDataOf: Set<HKSampleType>)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:).md)
  Tells the delegate that new data has been added to the builder.
- [func workoutBuilder(HKLiveWorkoutBuilder, didBegin: HKWorkoutActivity)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didbegin:).md)
  Tells the delegate that a new workout activity has started.
- [func workoutBuilder(HKLiveWorkoutBuilder, didEnd: HKWorkoutActivity)](hkliveworkoutbuilderdelegate/workoutbuilder(_:didend:).md)
  Tells the delegate that the current workout activity has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilderdidcollectevent(_:))*