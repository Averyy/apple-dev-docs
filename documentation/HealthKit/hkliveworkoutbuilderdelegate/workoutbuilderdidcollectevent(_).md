# workoutBuilderDidCollectEvent(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that a new event has been added to the builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS
- watchOS 5.0+

## Declaration

```swift
func workoutBuilderDidCollectEvent(_ workoutBuilder: HKLiveWorkoutBuilder)
```

```objc
- (void) workoutBuilderDidCollectEvent:(HKLiveWorkoutBuilder *) workoutBuilder;
```

## Mentions

- [Running workout sessions](../running-workout-sessions.md)

## See Also

### Receiving data updates
- [func workoutBuilder(HKLiveWorkoutBuilder, didCollectDataOf: Set<HKSampleType>)](./workoutbuilder%28_,didcollectdataof%29.md)
  Tells the delegate that new data has been added to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilderdidcollectevent(_:))*