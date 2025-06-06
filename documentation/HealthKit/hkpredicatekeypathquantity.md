# HKPredicateKeyPathQuantity

**Framework**: HealthKit  
**Kind**: var

The key path for accessing the sample’s quantity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKPredicateKeyPathQuantity: String
```

#### Discussion

Use this constant whenever you want to include a sample’s quantity in a predicate format string. Add a `%K` placeholder to the format string, and then pass this constant as an argument.

Alternatively, use the [`predicateForQuantitySamples(with:quantity:)`](hkquery/predicateforquantitysamples(with:quantity:).md) method to create predicates that match a sample’s quantity.

## See Also

- [let HKPredicateKeyPathCount: String](hkpredicatekeypathcount.md)
  A key path for the sample’s count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathquantity)*