# intersection(_:)

**Framework**: AppKit  
**Kind**: method

Returns the range, if any, where two text ranges intersect.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func intersection(_ textRange: NSTextRange) -> Self?
```

#### Return Value

An [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) that represents the intersection of the ranges, or `nil` if they don’t intersect.

## Parameters

- `textRange`: The range used to compare against the current range to evaluate for differences.

## See Also

- [func intersects(NSTextRange) -> Bool](nstextrange/intersects(_:).md)
  Determines if two ranges intersect.
- [func isEqual(to: NSTextRange) -> Bool](nstextrange/isequal(to:).md)
  Compares two text ranges.
- [func union(NSTextRange) -> Self](nstextrange/union(_:).md)
  Returns a new text range by forming the union with the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/intersection(_:))*