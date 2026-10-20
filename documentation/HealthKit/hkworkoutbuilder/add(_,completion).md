# add(_:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Adds a sample to be associated with the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func add(_ samples: [HKSample], completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func addSamples(_ samples: [HKSample]) async throws
```

```objc
- (void) addSamples:(NSArray<HKSample *> *) samples completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Mentions

- [Running workout sessions](../running-workout-sessions.md)

## See Also

### Associating samples with the workout
- [func seriesBuilder(for: HKSeriesType) -> HKSeriesBuilder?](./seriesbuilder%28for%29.md)
  Returns the series builder for the specified type, creating a new builder, if necessary.
- [func statistics(for: HKQuantityType) -> HKStatistics?](./statistics%28for%29.md)
  Returns the statistics calculated for matching samples added to the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/add(_:completion:))*