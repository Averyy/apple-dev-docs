# HKQuantityAggregationStyle.discreteEquivalentContinuousLevel

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

Discrete samples that can be combined over a time interval by computing the equivalent continuous sound level.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case discreteEquivalentContinuousLevel
```

```c
HKQuantityAggregationStyleDiscreteEquivalentContinuousLevel
```

## Discussion

For more information on sound level meters, see IEC 61672-1.

## See Also

### Aggregation Styles
- [HKQuantityAggregationStyle.cumulative](./cumulative.md)
  Cumulative samples that can be summed over time.
- [HKQuantityAggregationStyle.discreteArithmetic](./discretearithmetic.md)
  Discrete samples that can be averaged over time using an arithmetic mean.
- [HKQuantityAggregationStyle.discreteTemporallyWeighted](./discretetemporallyweighted.md)
  Discrete samples that can be averaged over a time interval using a temporally weighted integration function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle/discreteequivalentcontinuouslevel)*