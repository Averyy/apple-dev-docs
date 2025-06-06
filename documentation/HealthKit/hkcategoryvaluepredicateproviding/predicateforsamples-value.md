# predicateForSamples(_:value:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that checks a category sample’s value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func predicateForSamples(_ operatorType: NSComparisonPredicate.Operator, value: Self) -> NSPredicate
```

## Parameters

- `operatorType`: The type of operation to perform when matching the category sample’s value against the target value. For a list of possible operators, see  .
- `value`: The category sample’s target value. Use an enumeration value appropriate for the type of category samples you’re working with. For example, a predicate for sleep analysis samples use values from the   enumeration.

## See Also

- [static func predicateForSamples(equalTo: Set<Self>) -> NSPredicate](hkcategoryvaluepredicateproviding/predicateforsamples(equalto:).md)
  Returns a predicate that checks whether a category sample is equal to the provided set of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluepredicateproviding/predicateforsamples(_:value:))*