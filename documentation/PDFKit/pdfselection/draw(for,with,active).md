# draw(for:with:active:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Draws the selection relative to the origin of the specified box in page space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func draw(for page: PDFPage, with box: PDFDisplayBox, active: Bool)
```

```objc
- (void) drawForPage:(PDFPage *) page withBox:(PDFDisplayBox) box active:(BOOL) active;
```

#### Discussion

The selection is drawn using the current highlight color. If active is [`true`](../../Swift/true.md), drawing uses `selectedTextBackgroundColor`. If [`false`](../../Swift/false.md), it uses `secondarySelectedControlColor`. Refer to the [`PDFPage`](../pdfpage.md) class for the list of available box types.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Managing Selection Drawing
- [func draw(for: PDFPage, active: Bool)](./draw%28for,active%29.md)
  Calls [`draw(for:with:active:)`](./draw%28for,with,active%29.md) with a default value for box parameter.
- [var color: UIColor?](./color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/draw(for:with:active:))*