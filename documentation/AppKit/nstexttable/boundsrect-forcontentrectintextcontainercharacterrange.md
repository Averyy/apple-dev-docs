# boundsRect(for:contentRect:in:textContainer:characterRange:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle the text table block actually occupies, including padding, borders, and margins.

**Availability**:
- macOS ?+

## Declaration

```swift
func boundsRect(for block: NSTextTableBlock, contentRect: NSRect, in rect: NSRect, textContainer: NSTextContainer, characterRange charRange: NSRange) -> NSRect
```

#### Return Value

The rectangle the text table block actually occupies, including padding, borders, and margins.

#### Discussion

This method is called by the text table block `block` after it is laid out to determine the rectangle the text table block actually occupies, including padding, borders, and margins.

## Parameters

- `block`: The text table block that wants to determine where to layout its glyphs.
- `contentRect`: The actual rectangle in which the text was laid out, as determined by  .
- `rect`: The initial rectangle in   proposed by the typesetter.
- `textContainer`: The text container being used for the layout.
- `charRange`: The range of the characters whose glyphs are to be drawn.

## See Also

- [func rect(for: NSTextTableBlock, layoutAt: NSPoint, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](nstexttable/rect(for:layoutat:in:textcontainer:characterrange:).md)
  Returns the rectangle within which glyphs should be laid out for a text table block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttable/boundsrect(for:contentrect:in:textcontainer:characterrange:))*