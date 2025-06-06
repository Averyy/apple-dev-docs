# add(_:completion:)

**Framework**: HealthKit  
**Kind**: method

Adds a sample to be associated with the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func addSamples(_ samples: [HKSample]) async throws
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

## See Also

- [func seriesBuilder(for: HKSeriesType) -> HKSeriesBuilder?](hkworkoutbuilder/seriesbuilder(for:).md)
  Returns the series builder for the specified type, creating a new builder, if necessary.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkoutbuilder/statistics(for:).md)
  Returns the statistics calculated for matching samples added to the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/add(_:completion:))*