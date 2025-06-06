# predicateForQuantitySamples(with:quantity:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that matches samples based on the target quantity.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func predicateForQuantitySamples(with operatorType: NSComparisonPredicate.Operator, quantity: HKQuantity) -> NSPredicate
```

#### Return Value

A predicate that matches samples based on the target quantity. This predicate works only on quantity samples.

#### Discussion

Use this convenience method to create a predicate that matches against a sample’s quantity. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

## Parameters

- `operatorType`: The operator type to use when comparing the sample’s quantity to the target quantity.
- `quantity`: The target quantity object.

## See Also

- [let HKPredicateKeyPathQuantity: String](hkpredicatekeypathquantity.md)
  The key path for accessing the sample’s quantity.
- [var quantity: HKQuantity](hkquantitysample/quantity.md)
  The quantity for this sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforquantitysamples(with:quantity:))*