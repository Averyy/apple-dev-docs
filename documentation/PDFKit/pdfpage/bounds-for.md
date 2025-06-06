# bounds(for:)

**Framework**: PDFKit  
**Kind**: method

Returns the bounds for the specified PDF display box.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func bounds(for box: PDFDisplayBox) -> CGRect
```

#### Discussion

The [`PDFDisplayBox`](pdfdisplaybox.md) enumeration defines the various box types.

Note that only the media box is required for a PDF. If you request the bounds for the crop box, but the PDF does not include a crop box, the bounds for the media box are returned instead. If you request the bounds for other box types, and the PDF does not includes these types, the bounds for the crop box are returned instead.

The coordinates for the box are in page space, so you might need to transform the points if the page has a rotation on it. Also, note that the bounds `boundsForBox` returns are intersected with the page’s media box.

`boundsForBox` throws a range exception if `box` is not in range.

## See Also

- [class PDFPage](pdfpage.md)
  `PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.
- [var document: PDFDocument?](pdfpage/document.md)
  Returns the `PDFDocument` object with which the page is associated.
- [var label: String?](pdfpage/label.md)
  Returns the label for the page.
- [func setBounds(CGRect, for: PDFDisplayBox)](pdfpage/setbounds(_:for:).md)
  Sets the bounds for the specified box.
- [var rotation: Int](pdfpage/rotation.md)
  Sets the rotation angle for the page in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/bounds(for:))*