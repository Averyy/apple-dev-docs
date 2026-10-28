# boundsRect(forContentRect:in:textContainer:characterRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle the text in the block actually occupies, including padding, borders, and margins.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func boundsRect(forContentRect contentRect: NSRect, in rect: NSRect, textContainer: NSTextContainer, characterRange charRange: NSRange) -> NSRect
```

```objc
- (NSRect) boundsRectForContentRect:(NSRect) contentRect inRect:(NSRect) rect textContainer:(NSTextContainer *) textContainer characterRange:(NSRange) charRange;
```

## Return Value

The rectangle the text in the block actually occupies, including padding, borders, and margins.

## Discussion

This methods is called by the typesetter after the text block is laid out to return the rectangle the text in the block actually occupies, including padding, borders, and margins.

## Parameters

- `contentRect`: The actual rectangle in which the text was laid out, as determined by [`rectForLayout(at:in:textContainer:characterRange:)`](./rectforlayout%28at,in,textcontainer,characterrange%29.md).
- `rect`: The initial rectangle in `textContainer` proposed by the typesetter.
- `textContainer`: The text container being used for the layout.
- `charRange`: The range of the characters in the [`NSTextStorage`](../nstextstorage.md) object whose glyphs are to be drawn.

## See Also

### Determining size and position of a text block
- [func rectForLayout(at: NSPoint, in: NSRect, textContainer: NSTextContainer, characterRange: NSRange) -> NSRect](./rectforlayout%28at,in,textcontainer,characterrange%29.md)
  Returns the rectangle within which glyphs should be laid out for the specified arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/boundsrect(forcontentrect:in:textcontainer:characterrange:))*