# parent

**Framework**: PDFKit  
**Kind**: property

Returns the parent outline object of the outline (returns `NULL` if called on the root outline object).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var parent: PDFOutline? { get }
```

## See Also

- [var document: PDFDocument?](pdfoutline/document.md)
  Returns the document with which the outline is associated.
- [var numberOfChildren: Int](pdfoutline/numberofchildren.md)
  Returns the number of child outline objects in the outline.
- [func child(at: Int) -> PDFOutline?](pdfoutline/child(at:).md)
  Returns the child outline object at the specified index.
- [var index: Int](pdfoutline/index.md)
  Returns the index of the outline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/parent)*