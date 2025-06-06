# init(predicate:options:)

**Framework**: HealthKit  
**Kind**: init

Creates a statistics query descriptor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
init(predicate: HKSamplePredicate<HKQuantitySample>, options: HKStatisticsOptions)
```

## Parameters

- `predicate`: A predicate that defines the set of data that the query uses to calculate the statistics.
- `options`: A list of options that define the type of statistical calculations performed and the way in which HealthKit merges data from multiple sources. For a list of valid options, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsquerydescriptor/init(predicate:options:))*