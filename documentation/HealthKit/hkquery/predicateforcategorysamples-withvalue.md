# predicateForCategorySamples(with:value:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that checks a category sample’s value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForCategorySamples(with operatorType: NSComparisonPredicate.Operator, value: Int) -> NSPredicate
```

#### Return Value

A predicate that matches category samples based on the provided expression. This predicate works only with category samples.

#### Discussion

Use this convenience method to create a predicate that checks a category sample’s value. The following listing uses both the convenience method and a predicate format string to create equivalent predicates.

## Parameters

- `operatorType`: The type of operation to perform when matching the category sample’s value against the target value. For a list of possible operators, see  .
- `value`: The category sample’s target value. Use an enumeration value appropriate for the type of category samples you are working with. For example, a predicate for sleep analysis samples use values from the   enumeration.

## See Also

- [var value: Int](hkcategorysample/value.md)
  The category value for this sample.
- [let HKPredicateKeyPathCategoryValue: String](hkpredicatekeypathcategoryvalue.md)
  The key path for accessing the category sample’s value.
- [protocol HKCategoryValuePredicateProviding](hkcategoryvaluepredicateproviding.md)
  A protocol for objects that produce predicates that match category value samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforcategorysamples(with:value:))*