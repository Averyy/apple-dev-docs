# workoutBuilder(_:didCollectDataOf:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) workoutBuilder:(HKLiveWorkoutBuilder *) workoutBuilder didCollectDataOfTypes:(NSSet<HKSampleType *> *) collectedTypes;
```

## Mentions

- [Running workout sessions](../running-workout-sessions.md)

## See Also

### Receiving data updates
- [func workoutBuilderDidCollectEvent(HKLiveWorkoutBuilder)](./workoutbuilderdidcollectevent%28_%29.md)
  Tells the delegate that a new event has been added to the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:))*