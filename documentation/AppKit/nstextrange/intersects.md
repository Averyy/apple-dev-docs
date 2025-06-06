# intersects(_:)

**Framework**: AppKit  
**Kind**: method

Determines if two ranges intersect.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func intersects(_ textRange: NSTextRange) -> Bool
```

#### Return Value

Returns `true` if the ranges intersect.

## Parameters

- `textRange`: The range used to compare against the current range to evaluate for differences.

## See Also

- [func intersection(NSTextRange) -> Self?](nstextrange/intersection(_:).md)
  Returns the range, if any, where two text ranges intersect.
- [func isEqual(to: NSTextRange) -> Bool](nstextrange/isequal(to:).md)
  Compares two text ranges.
- [func union(NSTextRange) -> Self](nstextrange/union(_:).md)
  Returns a new text range by forming the union with the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/intersects(_:))*