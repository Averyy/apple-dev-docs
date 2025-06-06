# predicate

**Framework**: HealthKit  
**Kind**: property

A predicate that defines the set of data that the query uses to calculate the statistics.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
var predicate: HKSamplePredicate<HKQuantitySample>
```

## See Also

- [var options: HKStatisticsOptions](hkstatisticsquerydescriptor/options.md)
  A list of options that define the type of statistical calculations performed and the way in which HealthKit merges data from multiple sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsquerydescriptor/predicate)*