# rulerAttributes(in:)

**Framework**: Foundation  
**Kind**: method

Returns the ruler (paragraph) attributes in effect for the characters within the specified range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func rulerAttributes(in range: NSRange) -> [NSAttributedString.Key : Any]
```

#### Return Value

A dictionary containing the ruler attributes in the range.

#### Discussion

The only ruler attribute currently defined is that named by [`paragraphStyle`](nsattributedstring/key/paragraphstyle.md). Use this method to obtain attributes that are to be copied or pasted with “copy ruler” operations.

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: The range.

## See Also

- [func fontAttributes(in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/fontattributes(in:).md)
  Returns the font attributes in effect for the character at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/rulerattributes(in:))*