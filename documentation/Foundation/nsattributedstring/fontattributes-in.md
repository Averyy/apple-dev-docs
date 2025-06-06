# fontAttributes(in:)

**Framework**: Foundation  
**Kind**: method

Returns the font attributes in effect for the character at the specified location.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func fontAttributes(in range: NSRange) -> [NSAttributedString.Key : Any]
```

#### Return Value

A dictionary containing the font attributes for the range.

#### Discussion

The dictionary attributes are all those listed in `Character Attributes`, except [`link`](nsattributedstring/key/link.md), [`paragraphStyle`](nsattributedstring/key/paragraphstyle.md), and [`attachment`](nsattributedstring/key/attachment.md).

Use this method to obtain font attributes that are to be copied or pasted with “copy font” operations.

Raises an `NSRangeException` if any part of `aRange` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: The range.

## See Also

- [func rulerAttributes(in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/rulerattributes(in:).md)
  Returns the ruler (paragraph) attributes in effect for the characters within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/fontattributes(in:))*