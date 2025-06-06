# draw(for:active:)

**Framework**: PDFKit  
**Kind**: method

Calls [`draw(for:with:active:)`](pdfselection/draw(for:with:active:).md) with a default value for box parameter.

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

#### Discussion

The default value is `kPDFDisplayBoxCropBox`. If active is [`true`](https://developer.apple.com/documentation/swift/true), drawing uses `selectedTextBackgroundColor`. If [`false`](https://developer.apple.com/documentation/swift/false), it uses `secondarySelectedControlColor`.

## See Also

- [func draw(for: PDFPage, with: PDFDisplayBox, active: Bool)](pdfselection/draw(for:with:active:).md)
  Draws the selection relative to the origin of the specified box in page space.
- [var color: UIColor?](pdfselection/color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/draw(for:active:))*