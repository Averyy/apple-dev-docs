# MergeableDocument

**Framework**: Assignables  
**Kind**: protocol

Documents conforming to this protocol can merge several copies of the document into a single document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
protocol MergeableDocument : MergeablePartsContainer, Identifiable
```

## Topics

### Getting the pages
- [var pages: [Self.Page]](mergeabledocument/pages.md)
  The collection of pages in this document.
- [associatedtype Page : MergeableDocumentPage](mergeabledocument/page.md)
  The page type this document contains.
### Exporting the layers
- [func exportToPDF(visibleParts: [Self.PartID]) async -> PDFDocument](mergeabledocument/exporttopdf(visibleparts:).md)
  Exports the indicated layers of this document into a single `PDFDocument`.
### Exporting the thumbnails
- [func pageThumbnails(visibleParts: [Self.PartID]) async -> [Self.Page.ID : Self.Page.Thumbnail]](mergeabledocument/pagethumbnails(visibleparts:).md)
  Exports thumbnails of each page such that the thumbnails contain the indicated layers.
### Getting the error type
- [associatedtype Error : Error](mergeabledocument/error.md)
  The error type for this type.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MergeablePartsContainer](mergeablepartscontainer.md)
### Conforming Types
- [AssignableDocument](assignabledocument.md)
- [AssignedWorkDocument](assignedworkdocument.md)

## See Also

- [struct MergeablePartsContainerPartID](mergeablepartscontainerpartid.md)
  The ID of a part in a `MergeablePartsContainer`.
- [protocol MergeableDocumentPage](mergeabledocumentpage.md)
  Types conforming to this protocol indicate that they are a page in a [`MergeableDocument`](mergeabledocument.md) conforming object.
- [protocol MergeablePartsContainer](mergeablepartscontainer.md)
  Objects conforming to this protocol allow merging in other replicas of themselves or merging in individual parts of themselves.
- [struct DocumentThumbnail](documentthumbnail.md)
  A structure that contains an image of an entire page or a portion of a page and the ID of the page the image is from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeabledocument)*