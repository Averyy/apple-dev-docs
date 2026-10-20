# isEqual(to:)

**Framework**: UIKit  
**Kind**: method

Compares two text ranges.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func isEqual(to textRange: NSTextRange) -> Bool
```

#### Return Value

Returns `true` if the ranges are equal.

## Parameters

- `textRange`: The range used to compare against the current range to evaluate for differences.

## See Also

- [func intersection(NSTextRange) -> Self?](nstextrange/intersection(_:).md)
  Returns the range, if any, where two text ranges intersect.
- [func intersects(NSTextRange) -> Bool](nstextrange/intersects(_:).md)
  Determines if two ranges intersect.
- [func union(NSTextRange) -> Self](nstextrange/union(_:).md)
  Returns a new text range by forming the union with the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextrange/isequal(to:))*