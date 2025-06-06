# rectForLayout(at:in:textContainer:characterRange:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle within which glyphs should be laid out for the specified arguments.

**Availability**:
- macOS ?+

## Declaration

```swift
func rectForLayout(at startingPoint: NSPoint, in rect: NSRect, textContainer: NSTextContainer, characterRange charRange: NSRange) -> NSRect
```

#### Return Value

The rectangle within which glyphs should be laid out.

#### Discussion

This method is called by the typesetter before the text block is laid out to return the rectangle within which glyphs should be laid out.

## Parameters

- `startingPoint`: The location, in container coordinates, where layout begins.
- `rect`: The rectangle in which the block is constrained to lie. For top-level blocks, this is the container rectangle of  ; for nested blocks, this is the layout rectangle of the enclosing block.
- `textContainer`: The text container being used for the layout.
- `charRange`: The range of the characters in the   object whose glyphs are to be drawn.

## See Also

- [func boundsRect(forContentRect: NSRect, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](nstextblock/boundsrect(forcontentrect:in:textcontainer:characterrange:).md)
  Returns the rectangle the text in the block actually occupies, including padding, borders, and margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/rectforlayout(at:in:textcontainer:characterrange:))*