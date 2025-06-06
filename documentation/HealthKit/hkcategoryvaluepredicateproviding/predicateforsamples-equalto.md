# predicateForSamples(equalTo:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that checks whether a category sample is equal to the provided set of values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func predicateForSamples(equalTo values: Set<Self>) -> NSPredicate
```

## Parameters

- `values`: The target set of values.

## See Also

- [static func predicateForSamples(NSComparisonPredicate.Operator, value: Self) -> NSPredicate](hkcategoryvaluepredicateproviding/predicateforsamples(_:value:).md)
  Returns a predicate that checks a category sample’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluepredicateproviding/predicateforsamples(equalto:))*