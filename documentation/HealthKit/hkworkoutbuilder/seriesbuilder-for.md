# seriesBuilder(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the series builder for the specified type, creating a new builder, if necessary.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func seriesBuilder(for seriesType: HKSeriesType) -> HKSeriesBuilder?
```

## Mentions

- [Creating a workout route](creating-a-workout-route.md)

## See Also

- [func add([HKSample], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/add(_:completion:).md)
  Adds a sample to be associated with the workout.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkoutbuilder/statistics(for:).md)
  Returns the statistics calculated for matching samples added to the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/seriesbuilder(for:))*