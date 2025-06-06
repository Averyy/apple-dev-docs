# HKQuantityAggregationStyle.discreteArithmetic

**Framework**: HealthKit  
**Kind**: case

Discrete samples that can be averaged over time using an arithmetic mean.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case discreteArithmetic
```

#### Discussion

Use discrete types to monitor changes in a value over time. Body mass, heart rate, temperature, and respiratory rate are all discrete quantity types. You can also query for the minimum or maximum value in a given time period.

## See Also

- [HKQuantityAggregationStyle.cumulative](hkquantityaggregationstyle/cumulative.md)
  Cumulative samples that can be summed over time.
- [HKQuantityAggregationStyle.discreteTemporallyWeighted](hkquantityaggregationstyle/discretetemporallyweighted.md)
  Discrete samples that can be averaged over a time interval using a temporally weighted integration function.
- [HKQuantityAggregationStyle.discreteEquivalentContinuousLevel](hkquantityaggregationstyle/discreteequivalentcontinuouslevel.md)
  Discrete samples that can be combined over a time interval by computing the equivalent continuous sound level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle/discretearithmetic)*