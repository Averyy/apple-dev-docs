# is(compatibleWith:)

**Framework**: HealthKit  
**Kind**: method

Returns a Boolean value that indicates whether the quantity type is compatible with the given unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func `is`(compatibleWith unit: HKUnit) -> Bool
```

#### Return Value

YES if the quantity type is compatible with the given unit; otherwise, NO.

#### Discussion

When creating a HealthKit quantity sample, the sample’s type and quantity object must use compatible units. For more information, see [`HKQuantity`](hkquantity.md).

## Parameters

- `unit`: The HealthKit unit to be checked.

## See Also

- [var aggregationStyle: HKQuantityAggregationStyle](hkquantitytype/aggregationstyle.md)
  The aggregation style for the given quantity type.
- [enum HKQuantityAggregationStyle](hkquantityaggregationstyle.md)
  Constant values that describe how quantities can be aggregated over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytype/is(compatiblewith:))*