# compare(_:_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Provides the relative ordering of two elements based on the sort order of the comparator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func compare(_ lhs: Self.Compared, _ rhs: Self.Compared) -> ComparisonResult
```

#### Return Value

The relative ordering between the two elements according to the sort order of the comparator.

## Parameters

- `lhs`: The first element to compare.
- `rhs`: The second element to compare.

## See Also

- [associatedtype Compared](sortcomparator/compared.md)
  A type that the sort comparator can compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortcomparator/compare(_:_:))*