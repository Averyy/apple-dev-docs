# userName

**Framework**: PDFKit  
**Kind**: property

Returns the name of the user who created the annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var userName: String? { get set }
```

#### Return Value

The name of the user who created the annotation, or NULL if no user name is set.

## See Also

- [class PDFAnnotation](pdfannotation.md)
  An annotation in a PDF document.
- [var page: PDFPage?](pdfannotation/page.md)
  Returns the page that the annotation is associated with.
- [var modificationDate: Date?](pdfannotation/modificationdate.md)
  Returns the modification date of the annotation.
- [var type: String?](pdfannotation/type.md)
  Returns the type of the annotation.
- [var action: PDFAction?](pdfannotation/action.md)
  An object that represents an action for a PDF element, such as a link annotation.
- [class PDFAction](pdfaction.md)
  An action that is performed when, for example, a PDF annotation is activated or an outline item is clicked.
- [class PDFDestination](pdfdestination.md)
  A `PDFDestination` object describes a point on a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/username)*