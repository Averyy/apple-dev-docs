# intersects(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines if two ranges intersect.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func intersects(_ textRange: NSTextRange) -> Bool
```

```objc
- (BOOL) intersectsWithTextRange:(NSTextRange *) textRange;
```

#### Return Value

Returns `true` if the ranges intersect.

## Parameters

- `textRange`: The range used to compare against the current range to evaluate for differences.

## See Also

### Comparing text ranges
- [func intersection(NSTextRange) -> Self?](./intersection%28_%29.md)
  Returns the range, if any, where two text ranges intersect.
- [func isEqual(to: NSTextRange) -> Bool](./isequal%28to%29.md)
  Compares two text ranges.
- [func union(NSTextRange) -> Self](./union%28_%29.md)
  Returns a new text range by forming the union with the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/intersects(_:))*