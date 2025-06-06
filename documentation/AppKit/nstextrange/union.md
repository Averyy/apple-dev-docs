# union(_:)

**Framework**: AppKit  
**Kind**: method

Returns a new text range by forming the union with the text range you provide.

**Availability**:
- macOS 12.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/union(_:))*