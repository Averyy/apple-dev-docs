# workoutBuilder(_:didCollectDataOf:)

**Framework**: HealthKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that new data has been added to the builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- watchOS 5.0+

## Declaration

```swift
func workoutBuilder(_ workoutBuilder: HKLiveWorkoutBuilder, didCollectDataOf collectedTypes: Set<HKSampleType>)
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

## See Also

- [func workoutBuilderDidCollectEvent(HKLiveWorkoutBuilder)](hkliveworkoutbuilderdelegate/workoutbuilderdidcollectevent(_:).md)
  Tells the delegate that a new event has been added to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:))*