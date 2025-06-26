# AssignedWorkDocument

**Framework**: Assignables  
**Kind**: struct

An assigned work document is a document that contains taker and scorer markup specific to a taker. It also contains a copy of the assignable document upon which it is based.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct AssignedWorkDocument
```

#### Overview

This document has a collection of [`AssignedWorkDocument.ScoreAnnotation`](assignedworkdocument/scoreannotation.md) objects that represent marks such as correct and incorrect marks on a page. Score annotations are not automatically associated with a question defined in the `AssignableDocument` that this work document is based on. To determine the score for the work, you use `computeScore`.

You cannot instantiate this document type directly. Instead, you instantiate it by calling [`assign(to:)`](assignabledocument/assign(to:).md) or `makeAssignedWorkDocument()`.

This document is fully mergeable, which means that any copies of this document that are independently mutated can be merged into a determinisitic resulting document. You can merge copies of this document into this one using [`merge(_:)`](assignedworkdocument/merge(_:).md). You can also merge individual parts of copies of this document into this one with [`merge(partData:into:)`](assignedworkdocument/merge(partdata:into:).md). For example, if deviceA has documentA and deviceB has documentB, which is a copy of documentA. When a user changes a question in documentB on deviceB, deviceB can export that part’s data and send it to deviceA to be merged back into documentA.

You can create as many of these objects as you have memory for. This type assumes single-threaded access.

## Topics

### Creating an assigned work document
- [init(id: AssignedWorkDocument.ID, assignableDocument: AssignableDocument, partData: [AssignedWorkDocument.PartID : MergeablePartData]) async throws](assignedworkdocument/init(id:assignabledocument:partdata:)-8eh38.md)
  Construct an instance of this object with the parts data passed in.
- [init(id: AssignedWorkDocument.ID, assignableDocument: AssignableDocument, partData: [AssignedWorkDocument.PartID : URL]) throws](assignedworkdocument/init(id:assignabledocument:partdata:)-54yg5.md)
  Construct an instance of this object with the parts data passed in.
### Inspecting a work document
- [AssignedWorkDocument.ID](assignedworkdocument/id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignedWorkDocument.ID](assignedworkdocument/id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](assignedworkdocument/ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](assignedworkdocument/ispartial.md)
  Denotes whether or not this document is a partial one.
- [AssignedWorkDocument.PartIDs](assignedworkdocument/partids-swift.enum.md)
  An enumeration containing the identities of parts managed by this view.
- [var partIDs: [MergeablePartsContainerPartID]](assignedworkdocument/partids-swift.property.md)
  Returns a collection of identifiers reflecting the manifest of parts available in the document.
- [var scoreAnnotations: [AssignedWorkDocument.ScoreAnnotation]](assignedworkdocument/scoreannotations.md)
  The collection of score annotations for this work document. Treated as a multiset. i.e. The order of the elements doesn’t matter and duplicate values are allowed.
- [var scorers: [AnyUserIdentity]](assignedworkdocument/scorers.md)
  The identities of users scoring this assigned work. Treated as a set.
- [var pagesDebugDescription: String](assignedworkdocument/pagesdebugdescription.md)
- [AssignedWorkDocument.Error](assignedworkdocument/error.md)
  Errors for this document type.
### Getting the assignable document
- [var assignableDocument: AssignableDocument](assignedworkdocument/assignabledocument.md)
  The assignable document that this work document is based on.
### Getting the assignees
- [var assignees: [AnyUserIdentity]](assignedworkdocument/assignees.md)
  The identities of takers of this document. Treated as a set.
### Getting the configuration
- [AssignedWorkDocument.Configuration](assignedworkdocument/configuration-swift.typealias.md)
  The configuration for an assessment taker work which contains an optional manual score for the document.
- [var configuration: any AssignedWorkDocumentConfiguration](assignedworkdocument/configuration-swift.property.md)
  The configuration for a taker work which contains an optional manual score for the document.
### Merging the parts
- [func merge(AssignedWorkDocument) async throws -> Bool](assignedworkdocument/merge(_:).md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: AssignedWorkDocument.PartID) async throws -> Bool](assignedworkdocument/merge(partdata:into:).md)
  Merges an individual part into the specified part of this object.
- [func merge(other: AssignedWorkDocument) throws -> Bool](assignedworkdocument/merge(other:).md)
  Merge another object of this type into this object.
- [func merge(partID: AssignedWorkDocument.PartID, partDataURL: URL) throws -> Bool](assignedworkdocument/merge(partid:partdataurl:).md)
  Merges an individual part’s data into the specified part of this object.
### Producing thumbnails
- [func questionThumbnails(visibleParts: [AssignedWorkDocument.PartID]) async -> [AssignableDocument.Question.ID : [AssignableDocument.Question.Thumbnail]]](assignedworkdocument/questionthumbnails(visibleparts:).md)
  Produces thumbnails of question regions within the document.
### Computing the score
- [func computeScore() -> Double](assignedworkdocument/computescore.md)
  Gathers all of the points based on all the `AssignedWorkDocument.ScoreAnnotation`s in the document and its `kind` property.
- [AssignedWorkDocument.ScoreAnnotation](assignedworkdocument/scoreannotation.md)
  A score mark on page of the work document.
### Making the parts
- [func makePart(for: AssignedWorkDocument.PartID) throws -> MergeablePartData?](assignedworkdocument/makepart(for:).md)
  Creates data for the part with the given identifier.
### Exporting the parts
- [func exportParts(identifiedBy: [AssignedWorkDocument.PartID]) async throws -> [AssignedWorkDocument.PartID : MergeablePartData]](assignedworkdocument/exportparts(identifiedby:).md)
  Given a set of part identifiers, return a dictionary of part ID to part data.
- [func export(partIDs: [AssignedWorkDocument.PartID]) async throws -> [AssignedWorkDocument.PartID : URL]](assignedworkdocument/export(partids:).md)
  Given a set of part identifiers, return a dictionary of part ID to data objects for the requested parts.
### Comparing work documents
- [static func == (AssignedWorkDocument, AssignedWorkDocument) -> Bool](assignedworkdocument/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Hashing the work document
- [var hashValue: Int](assignedworkdocument/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](assignedworkdocument/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Accessing work documents
- [subscript(AssignedWorkDocument.Page.ID) -> AssignedWorkDocument.Page?](assignedworkdocument/subscript(_:)-4srtw.md)
  Access the page that the ID points to, if any.
- [subscript(AssignedWorkDocument.ScoreAnnotation.ID) -> AssignedWorkDocument.ScoreAnnotation?](assignedworkdocument/subscript(_:)-5h89c.md)
  Access the score annotation that the identifier refers to, if any.
### Default Implementations
- [Equatable Implementations](assignedworkdocument/equatable-implementations.md)
- [MergeableDocument Implementations](assignedworkdocument/mergeabledocument-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MergeableDocument](mergeabledocument.md)
- [MergeablePartsContainer](mergeablepartscontainer.md)

## See Also

- [struct AssignableDocument](assignabledocument.md)
  An assignable document is an augmented PDF that allows teachers to mark up the PDF with the intention of students taking the assessment.
- [protocol Assignable](assignable.md)
  Documents conforming to this protocol can be assigned to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument)*