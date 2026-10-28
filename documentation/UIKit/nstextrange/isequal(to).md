# isEqual(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isEqualToTextRange:(NSTextRange *) textRange;
```

## Return Value

Returns `true` if the ranges are equal.

## Parameters

- `textRange`: The range used to compare against the current range to evaluate for differences.

## See Also

### Comparing text ranges
- [func intersection(NSTextRange) -> Self?](./intersection%28_%29.md)
  Returns the range, if any, where two text ranges intersect.
- [func intersects(NSTextRange) -> Bool](./intersects%28_%29.md)
  Determines if two ranges intersect.
- [func union(NSTextRange) -> Self](./union%28_%29.md)
  Returns a new text range by forming the union with the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextrange/isequal(to:))*