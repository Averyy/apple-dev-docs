# draw(for:active:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Calls [`draw(for:with:active:)`](./draw%28for,with,active%29.md) with a default value for box parameter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func draw(for page: PDFPage, active: Bool)
```

```objc
- (void) drawForPage:(PDFPage *) page active:(BOOL) active;
```

## Discussion

The default value is `kPDFDisplayBoxCropBox`. If active is [`true`](../../Swift/true.md), drawing uses `selectedTextBackgroundColor`. If [`false`](../../Swift/false.md), it uses `secondarySelectedControlColor`.

## See Also

### Managing Selection Drawing
- [func draw(for: PDFPage, with: PDFDisplayBox, active: Bool)](./draw%28for,with,active%29.md)
  Draws the selection relative to the origin of the specified box in page space.
- [var color: UIColor?](./color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/draw(for:active:))*