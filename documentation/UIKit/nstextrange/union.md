# union(_:)

**Framework**: UIKit  
**Kind**: method

Returns a new text range by forming the union with the text range you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func union(_ textRange: NSTextRange) -> Self
```

#### Return Value

An [`NSTextRange`](nstextrange.md) that represent the union of the two ranges.

## Parameters

- `textRange`: The range to use to create the union.

## See Also

- [func intersection(NSTextRange) -> Self?](nstextrange/intersection(_:).md)
  Returns the range, if any, where two text ranges intersect.
- [func intersects(NSTextRange) -> Bool](nstextrange/intersects(_:).md)
  Determines if two ranges intersect.
- [func isEqual(to: NSTextRange) -> Bool](nstextrange/isequal(to:).md)
  Compares two text ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextrange/union(_:))*