# MergeablePartsContainer

**Framework**: Assignables  
**Kind**: protocol  
**Role**: Protocol

Objects conforming to this protocol allow merging in other replicas of themselves or merging in individual parts of themselves.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
protocol MergeablePartsContainer : Hashable
```

## Topics

### Merging the parts
- [func merge(other: Self) throws -> Bool](./mergeablepartscontainer/merge%28other%29.md)
  Merge another object of this type into this object.
- [func merge(partID: Self.PartID, partDataURL: URL) throws -> Bool](./mergeablepartscontainer/merge%28partid,partdataurl%29.md)
  Merges an individual part into the specified part of this object.
### Exporting the parts
- [func export(partIDs: [Self.PartID]) async throws -> [Self.PartID : URL]](./mergeablepartscontainer/export%28partids%29.md)
  Given a set of part identifiers, return a dictionary of part ID to URL to the part data file for the requested parts.
### Getting the part identifiers
- [var partIDs: [Self.PartID]](./mergeablepartscontainer/partids.md)
  Returns a collection of part IDs reflecting the manifest of parts available in the document.
- [MergeablePartsContainer.PartID](./mergeablepartscontainer/partid.md)
  The type for document layer IDs.
### Inspecting the parts
- [var isPartial: Bool](./mergeablepartscontainer/ispartial.md)
  Documents are considered partial when they are reconstituted missing one or more of their associated document part IDs. When a document is considered partial it is expected that we shouldn’t be able to both read or write to the parts that the document has neither been reconstituted or merged with.
### Instance Methods
- [func exportParts(identifiedBy: [Self.PartID]) async throws -> [Self.PartID : MergeablePartData]](./mergeablepartscontainer/exportparts%28identifiedby%29.md)
  Given a set of part identifiers, return a dictionary of part ID to part data.
- [func makePart(for: Self.PartID) throws -> MergeablePartData?](./mergeablepartscontainer/makepart%28for%29.md)
  Creates data for the part with the given identifier.
- [func merge(Self) async throws -> Bool](./mergeablepartscontainer/merge%28_%29.md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: Self.PartID) async throws -> Bool](./mergeablepartscontainer/merge%28partdata,into%29.md)
  Merges an individual part into the specified part of this object.

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
### Inherited By
- [MergeableDocument](./mergeabledocument.md)
### Conforming Types
- [AssignableDocument](./assignabledocument.md)
- [AssignedWorkDocument](./assignedworkdocument.md)

## See Also

### Mergeable document
- [protocol MergeableDocument](./mergeabledocument.md)
  Documents conforming to this protocol can merge several copies of the document into a single document.
- [struct MergeablePartsContainerPartID](./mergeablepartscontainerpartid.md)
  The ID of a part in a `MergeablePartsContainer`.
- [protocol MergeableDocumentPage](./mergeabledocumentpage.md)
  Types conforming to this protocol indicate that they are a page in a [`MergeableDocument`](./mergeabledocument.md) conforming object.
- [struct DocumentThumbnail](./documentthumbnail.md)
  A structure that contains an image of an entire page or a portion of a page and the ID of the page the image is from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartscontainer)*