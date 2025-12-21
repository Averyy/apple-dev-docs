# draw(for:with:active:)

**Framework**: PDFKit  
**Kind**: method

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

#### Discussion

The selection is drawn using the current highlight color. If active is [`true`](https://developer.apple.com/documentation/Swift/true), drawing uses `selectedTextBackgroundColor`. If [`false`](https://developer.apple.com/documentation/Swift/false), it uses `secondarySelectedControlColor`. Refer to the [`PDFPage`](pdfpage.md) class for the list of available box types.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [func draw(for: PDFPage, active: Bool)](pdfselection/draw(for:active:).md)
  Calls [`draw(for:with:active:)`](pdfselection/draw(for:with:active:).md) with a default value for box parameter.
- [var color: UIColor?](pdfselection/color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/draw(for:with:active:))*