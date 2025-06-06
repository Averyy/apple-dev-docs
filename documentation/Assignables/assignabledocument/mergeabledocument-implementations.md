# MergeableDocument Implementations

**Framework**: Assignables

## Topics

### Structures
- [AssignableDocument.Page](assignabledocument/page.md)
  A page within this assignable document.
### Instance Properties
- [var pages: [AssignableDocument.Page]](assignabledocument/pages.md)
  The collection of pages in this document.
### Instance Methods
- [func exportToPDF(visibleParts: [MergeablePartsContainerPartID]) async -> PDFDocument](assignabledocument/exporttopdf(visibleparts:).md)
  Exports the indicated parts of this document into a single `PDFDocument`.
- [func pageThumbnails(visibleParts: [MergeablePartsContainerPartID]) async -> [Self.Page.ID : Self.Page.Thumbnail]](assignabledocument/pagethumbnails(visibleparts:).md)
  Exports thumbnails of each page such that the thumbnails contain the indicated layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/mergeabledocument-implementations)*