# boundsRect(for:contentRect:in:textContainer:characterRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle the text table block actually occupies, including padding, borders, and margins.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func boundsRect(for block: NSTextTableBlock, contentRect: NSRect, in rect: NSRect, textContainer: NSTextContainer, characterRange charRange: NSRange) -> NSRect
```

```objc
- (NSRect) boundsRectForBlock:(NSTextTableBlock *) block contentRect:(NSRect) contentRect inRect:(NSRect) rect textContainer:(NSTextContainer *) textContainer characterRange:(NSRange) charRange;
```

#### Return Value

The rectangle the text table block actually occupies, including padding, borders, and margins.

#### Discussion

This method is called by the text table block `block` after it is laid out to determine the rectangle the text table block actually occupies, including padding, borders, and margins.

## Parameters

- `block`: The text table block that wants to determine where to layout its glyphs.
- `contentRect`: The actual rectangle in which the text was laid out, as determined by [`rectForLayout(at:in:textContainer:characterRange:)`](../nstextblock/rectforlayout%28at,in,textcontainer,characterrange%29.md).
- `rect`: The initial rectangle in `textContainer` proposed by the typesetter.
- `textContainer`: The text container being used for the layout.
- `charRange`: The range of the characters whose glyphs are to be drawn.

## See Also

### Determining layout rectangles
- [func rect(for: NSTextTableBlock, layoutAt: NSPoint, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](./rect%28for,layoutat,in,textcontainer,characterrange%29.md)
  Returns the rectangle within which glyphs should be laid out for a text table block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttable/boundsrect(for:contentrect:in:textcontainer:characterrange:))*