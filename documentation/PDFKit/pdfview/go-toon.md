# go(to:on:)

**Framework**: PDFKit  
**Kind**: method

Navigates to the specified rectangle on the specified page.

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
func go(to rect: NSRect, on page: PDFPage)
```

#### Discussion

If the specified rectangle is already visible, this method does nothing. This allows you to scroll the `PDFView` object to a specific [`PDFAnnotation`](pdfannotation.md) or [`PDFSelection`](pdfselection.md) object, because both of these objects have bounds methods that return an annotation or selection position in page space.

Note that `rect` is specified in page-space coordinates. Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [func go(to: PDFPage)](pdfview/go(to:)-6x8y2.md)
  Scrolls to the specified page.
- [func go(to: PDFDestination)](pdfview/go(to:)-5lh5d.md)
  Navigates to the specified destination.
- [func go(to: PDFSelection)](pdfview/go(to:)-3t5go.md)
  Scrolls to the first character of the specified selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/go(to:on:))*