# indexRange(in:)

**Framework**: Foundation  
**Kind**: method

Return a `Range<IndexSet.Index>` which can be used to subscript the index set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func indexRange<R>(in range: R) -> Range<IndexSet.Index> where R : RangeExpression, R.Bound == Int
```

#### Discussion

The resulting range is the range of the intersection of the integers in `range` with the index set.

## Parameters

- `range`: The range of integers to include.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/indexrange(in:)-6057o)*