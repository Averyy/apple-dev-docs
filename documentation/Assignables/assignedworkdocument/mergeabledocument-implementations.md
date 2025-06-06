# MergeableDocument Implementations

**Framework**: Assignables

## Topics

### Structures
- [AssignedWorkDocument.Page](assignedworkdocument/page.md)
  A page within this assigned work document.
### Instance Properties
- [var pages: [AssignedWorkDocument.Page]](assignedworkdocument/pages.md)
  The collection of pages in this document.
### Instance Methods
- [func exportToPDF(visibleParts: [MergeablePartsContainerPartID]) async -> PDFDocument](assignedworkdocument/exporttopdf(visibleparts:).md)
  Exports the indicated layers of this document into a single `PDFDocument`.
- [func pageThumbnails(visibleParts: [MergeablePartsContainerPartID]) async -> [Self.Page.ID : Self.Page.Thumbnail]](assignedworkdocument/pagethumbnails(visibleparts:).md)
  Exports thumbnails of each page such that the thumbnails contain the indicated layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/mergeabledocument-implementations)*