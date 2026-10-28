# drawCharacters(in:forContentView:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draw the glyphs for the requested character range as they are drawn in the given content view.

**Availability**:
- macOS

## Declaration

```swift
optional func drawCharacters(in range: NSRange, forContentView view: NSView)
```

```objc
- (void) drawCharactersInRange:(NSRange) range forContentView:(NSView *) view;
```

## Discussion

If the character range partially intersects a glyph range, then the full glyph is drawn to avoid additional layout.

The given range is guaranteed to be completely contained by the given view. When this method is called, a drawing context effectively identical to the one provided to the view’s [`draw(_:)`](../nsview/draw%28_%29.md) method is configured. This method is mainly used to draw find indicator contents, so implementations should check -the view property [`isDrawingFindIndicator`](../nsview/isdrawingfindindicator.md) to ensure that the text will be easily readable against the background of the find indicator when it returns [`true`](../../Swift/true.md). If this method is not implemented, then the find indicator will be drawn using the content view’s [`draw(_:)`](../nsview/draw%28_%29.md) method instead.

## Parameters

- `range`: The character range.
- `view`: The content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/drawcharacters(in:forcontentview:))*