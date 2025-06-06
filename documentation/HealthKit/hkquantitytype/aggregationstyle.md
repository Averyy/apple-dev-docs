# aggregationStyle

**Framework**: HealthKit  
**Kind**: property

The aggregation style for the given quantity type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var aggregationStyle: HKQuantityAggregationStyle { get }
```

#### Discussion

For more information on aggregation styles, see [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md).

## See Also

- [enum HKQuantityAggregationStyle](hkquantityaggregationstyle.md)
  Constant values that describe how quantities can be aggregated over time.
- [func `is`(compatibleWith: HKUnit) -> Bool](hkquantitytype/is(compatiblewith:).md)
  Returns a Boolean value that indicates whether the quantity type is compatible with the given unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytype/aggregationstyle)*