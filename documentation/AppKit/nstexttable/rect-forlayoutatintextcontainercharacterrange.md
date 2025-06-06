# rect(for:layoutAt:in:textContainer:characterRange:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle within which glyphs should be laid out for a text table block.

**Availability**:
- macOS ?+

## Declaration

```swift
func rect(for block: NSTextTableBlock, layoutAt startingPoint: NSPoint, in rect: NSRect, textContainer: NSTextContainer, characterRange charRange: NSRange) -> NSRect
```

#### Return Value

The rectangle within which glyphs should be laid out.

#### Discussion

This method is called by the text table block `block` to determine the rectangle within which glyphs should be laid out for the text table block.

## Parameters

- `block`: The text table block that wants to determine where to layout its glyphs.
- `startingPoint`: The location, in container coordinates, where layout begins.
- `rect`: The rectangle in which the block is constrained to lie. For top-level blocks, this is the container rectangle of  ; for nested blocks, this is the layout rectangle of the enclosing block.
- `textContainer`: The text container being used for the layout.
- `charRange`: The range of the characters whose glyphs are to be drawn.

## See Also

- [func boundsRect(for: NSTextTableBlock, contentRect: NSRect, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](nstexttable/boundsrect(for:contentrect:in:textcontainer:characterrange:).md)
  Returns the rectangle the text table block actually occupies, including padding, borders, and margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttable/rect(for:layoutat:in:textcontainer:characterrange:))*