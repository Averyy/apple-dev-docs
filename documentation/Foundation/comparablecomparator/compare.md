# compare(_:_:)

**Framework**: Foundation  
**Kind**: method

Provides the relative ordering of two elements.

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
func compare(_ lhs: Compared, _ rhs: Compared) -> ComparisonResult
```

#### Return Value

The relative ordering between the two elements.

#### Discussion

The method returns flipped comparisons if the sort order is [`SortOrder.reverse`](sortorder/reverse.md).

## Parameters

- `lhs`: The first element to compare.
- `rhs`: The second element to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/comparablecomparator/compare(_:_:))*