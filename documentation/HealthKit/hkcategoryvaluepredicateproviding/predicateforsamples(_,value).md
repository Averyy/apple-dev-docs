# predicateForSamples(_:value:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that checks a category sample’s value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
static func predicateForSamples(_ operatorType: NSComparisonPredicate.Operator, value: Self) -> NSPredicate
```

Available when `RawValue` is `Int`.

## Parameters

- `operatorType`: The type of operation to perform when matching the category sample’s value against the target value. For a list of possible operators, see [`NSComparisonPredicate.Operator.contains`](../../Foundation/nscomparisonpredicate/operator/contains.md).
- `value`: The category sample’s target value. Use an enumeration value appropriate for the type of category samples you’re working with. For example, a predicate for sleep analysis samples use values from the [`HKCategoryValueSleepAnalysis`](../hkcategoryvaluesleepanalysis.md) enumeration.

## See Also

### Creating predicates
- [static func predicateForSamples(equalTo: Set<Self>) -> NSPredicate](./predicateforsamples%28equalto%29.md)
  Returns a predicate that checks whether a category sample is equal to the provided set of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluepredicateproviding/predicateforsamples(_:value:))*