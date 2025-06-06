# statistics(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the statistics calculated for matching samples added to the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func statistics(for quantityType: HKQuantityType) -> HKStatistics?
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

## See Also

- [func add([HKSample], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/add(_:completion:).md)
  Adds a sample to be associated with the workout.
- [func seriesBuilder(for: HKSeriesType) -> HKSeriesBuilder?](hkworkoutbuilder/seriesbuilder(for:).md)
  Returns the series builder for the specified type, creating a new builder, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/statistics(for:))*