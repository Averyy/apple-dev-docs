# action

**Framework**: PDFKit  
**Kind**: property

An object that represents an action for a PDF element, such as a link annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var action: PDFAction? { get set }
```

## See Also

- [var page: PDFPage?](pdfannotation/page.md)
  Returns the page that the annotation is associated with.
- [var modificationDate: Date?](pdfannotation/modificationdate.md)
  Returns the modification date of the annotation.
- [var userName: String?](pdfannotation/username.md)
  Returns the name of the user who created the annotation.
- [var type: String?](pdfannotation/type.md)
  Returns the type of the annotation.
- [class PDFAction](pdfaction.md)
  An action that is performed when, for example, a PDF annotation is activated or an outline item is clicked.
- [class PDFDestination](pdfdestination.md)
  A `PDFDestination` object describes a point on a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/action)*