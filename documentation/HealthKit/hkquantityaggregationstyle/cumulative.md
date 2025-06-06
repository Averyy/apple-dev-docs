# HKQuantityAggregationStyle.cumulative

**Framework**: HealthKit  
**Kind**: case

Cumulative samples that can be summed over time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case cumulative
```

#### Discussion

Use cumulative types to measure a total value over a given time period. Step count, distance, inhaler usage, nutritional information, and energy burned are all cumulative quantity types.

## See Also

- [HKQuantityAggregationStyle.discreteArithmetic](hkquantityaggregationstyle/discretearithmetic.md)
  Discrete samples that can be averaged over time using an arithmetic mean.
- [HKQuantityAggregationStyle.discreteTemporallyWeighted](hkquantityaggregationstyle/discretetemporallyweighted.md)
  Discrete samples that can be averaged over a time interval using a temporally weighted integration function.
- [HKQuantityAggregationStyle.discreteEquivalentContinuousLevel](hkquantityaggregationstyle/discreteequivalentcontinuouslevel.md)
  Discrete samples that can be combined over a time interval by computing the equivalent continuous sound level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle/cumulative)*