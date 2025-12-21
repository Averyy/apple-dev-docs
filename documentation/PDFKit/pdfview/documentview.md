# documentView

**Framework**: PDFKit  
**Kind**: property

The innermost view used by `PDFView` or by your `PDFView` subclass.

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
var documentView: NSView? { get }
```

#### Discussion

The innermost view is the one displaying the visible document pages. This method is useful when converting coordinates from one view to another.

## See Also

- [func layoutDocumentView()](pdfview/layoutdocumentview.md)
  Performs layout of the inner views.
- [Draw Operations](draw-operations.md)
  Draw in a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/documentview)*