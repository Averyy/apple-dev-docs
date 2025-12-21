# rangeView(of:)

**Framework**: Foundation  
**Kind**: method

Returns a `Range`-based view of `self`.

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
func rangeView<R>(of range: R) -> IndexSet.RangeView where R : RangeExpression, R.Bound == Int
```

## Parameters

- `range`: A subrange of   to view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/rangeview(of:)-4jdy1)*