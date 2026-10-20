# compare(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Compares two values after converting them to the same units.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func compare(_ quantity: HKQuantity) -> ComparisonResult
```

```objc
- (NSComparisonResult) compare:(HKQuantity *) quantity;
```

#### Return Value

[`ComparisonResult.orderedDescending`](../../Foundation/comparisonresult/ordereddescending.md) if the parameter is less than the receiver. [`ComparisonResult.orderedAscending`](../../Foundation/comparisonresult/orderedascending.md) if the parameter is greater than the receiver. [`ComparisonResult.orderedSame`](../../Foundation/comparisonresult/orderedsame.md) if the quantities are equal.

#### Discussion

Returns whether the quantity argument is less than, equal to, or greater than the current quantity. This method automatically converts the quantities into the same units before comparing the values. You just need to ensure that the quantities have compatible units.

> **Note**:  Converting a value to a different unit can introduce floating point errors. Values that should be equal may appear unequal due to these floating point errors.

In most cases, the compatible units are clear from context. To see the unit types associated with different quantity sample types, see the type identifiers in [`HKQuantityTypeIdentifier`](../hkquantitytypeidentifier.md).

If you need to programmatically check whether a particular unit is compatible with a particular quantity, call the quantity’s [`is(compatibleWith:)`](./is%28compatiblewith%29.md) method.

## Parameters

- `quantity`: The quantity to compare. This method throws an exception if the quantities do not have compatible units ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)).

## See Also

### Related Documentation
- [func `is`(compatibleWith: HKUnit) -> Bool](./is%28compatiblewith%29.md)
  Returns a boolean value indicating whether the quantity is compatible with the provided unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantity/compare(_:))*