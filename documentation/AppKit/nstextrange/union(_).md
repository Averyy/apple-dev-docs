# union(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new text range by forming the union with the text range you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func union(_ textRange: NSTextRange) -> Self
```

```objc
- (instancetype) textRangeByFormingUnionWithTextRange:(NSTextRange *) textRange;
```

## Return Value

An [`NSTextRange`](../nstextrange.md) that represent the union of the two ranges.

## Parameters

- `textRange`: The range to use to create the union.

## See Also

### Comparing text ranges
- [func intersection(NSTextRange) -> Self?](./intersection%28_%29.md)
  Returns the range, if any, where two text ranges intersect.
- [func intersects(NSTextRange) -> Bool](./intersects%28_%29.md)
  Determines if two ranges intersect.
- [func isEqual(to: NSTextRange) -> Bool](./isequal%28to%29.md)
  Compares two text ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/union(_:))*