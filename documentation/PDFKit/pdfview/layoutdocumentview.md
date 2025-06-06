# layoutDocumentView()

**Framework**: PDFKit  
**Kind**: method

Performs layout of the inner views.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func layoutDocumentView()
```

#### Discussion

The `PDFView` actually contains several subviews, such as the document view (where the PDF is actually drawn) and a “matte view” (which may appear as a gray area around the PDF content, depending on the scaling). Changes to the PDF content may require changes to these inner views, so you must call this method explicitly if you use PDF Kit utility classes to add or remove a page, rotate a page, or perform other operations affecting visible layout.

This method is called automatically from `PDFView` methods that affect the visible layout (such as `setDocument(_:)`, `setDisplayBox(_:)` or [`zoomIn(_:)`](pdfview/zoomin(_:).md)).

## See Also

- [var documentView: UIView?](pdfview/documentview.md)
  The innermost view used by `PDFView` or by your `PDFView` subclass.
- [Draw Operations](draw-operations.md)
  Draw in a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/layoutdocumentview())*