# intersection(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the range, if any, where two text ranges intersect.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func intersection(_ textRange: NSTextRange) -> Self?
```

```objc
- (instancetype) textRangeByIntersectingWithTextRange:(NSTextRange *) textRange;
```

#### Return Value

An [`NSRange`](../../Foundation/nsrange-c.struct.md) that represents the intersection of the ranges, or `nil` if they don’t intersect.

## Parameters

- `textRange`: The range used to compare against the current range to evaluate for differences.

## See Also

### Comparing text ranges
- [func intersects(NSTextRange) -> Bool](./intersects%28_%29.md)
  Determines if two ranges intersect.
- [func isEqual(to: NSTextRange) -> Bool](./isequal%28to%29.md)
  Compares two text ranges.
- [func union(NSTextRange) -> Self](./union%28_%29.md)
  Returns a new text range by forming the union with the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/intersection(_:))*