# doubleValue(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the quantity’s value in the provided unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func doubleValue(for unit: HKUnit) -> Double
```

#### Return Value

The quantity’s value in the provided units.

#### Discussion

This method converts the quantity’s value to the desired units. You do not need to know the quantity’s original units. You can request the value in whatever units you want, as long as they are compatible with the quantity. This lets each application (or each locale) work with its preferred units.

In most cases, you know which units are compatible with a given quantity from context. To see the unit types associated with different quantity sample types, see the type identifiers in [`HKQuantityTypeIdentifier`](hkquantitytypeidentifier.md).

If you need to programmatically check whether a particular unit is compatible with a particular quantity, call the quantity’s [`is(compatibleWith:)`](hkquantity/is(compatiblewith:).md) method.

## Parameters

- `unit`: The target unit. If the quantity is not compatible with this unit, it throws an exception ( ).

## See Also

- [func `is`(compatibleWith: HKUnit) -> Bool](hkquantity/is(compatiblewith:).md)
  Returns a boolean value indicating whether the quantity is compatible with the provided unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantity/doublevalue(for:))*