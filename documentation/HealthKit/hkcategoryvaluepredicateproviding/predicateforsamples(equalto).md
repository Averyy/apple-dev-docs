# predicateForSamples(equalTo:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that checks whether a category sample is equal to the provided set of values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
static func predicateForSamples(equalTo values: Set<Self>) -> NSPredicate
```

Available when `RawValue` is `Int`.

## Parameters

- `values`: The target set of values.

## See Also

### Creating predicates
- [static func predicateForSamples(NSComparisonPredicate.Operator, value: Self) -> NSPredicate](./predicateforsamples%28_,value%29.md)
  Returns a predicate that checks a category sample’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluepredicateproviding/predicateforsamples(equalto:))*