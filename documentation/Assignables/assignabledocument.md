# AssignableDocument

**Framework**: Assignables  
**Kind**: struct

An assignable document is an augmented PDF that allows teachers to mark up the PDF with the intention of students taking the assessment.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct AssignableDocument
```

#### Overview

The document has several parts, which includes the ability to modify the PDF, annotate the PDF, and define question regions in the PDF.

To add a question to this assignable, you can use [`appendQuestion(pageID:rect:maxScore:)`](assignabledocument/appendquestion(pageid:rect:maxscore:).md) which will take care of associating a box to a page and adding a question connected to that box to the document.

This document is fully mergeable, which means that any copies of this document that are independently mutated can be merged into a determinisitic resulting document. You can merge copies of this document into this one using [`merge(_:)`](assignabledocument/merge(_:).md). You can also merge individual parts of copies of this document into this one with [`merge(partData:into:)`](assignabledocument/merge(partdata:into:).md). For example, if deviceA has documentA and deviceB has documentB, which is a copy of documentA. When a user changes a question in documentB on deviceB, deviceB can export that part’s data and send it to deviceA to be merged back into documentA.

You can create as many of these objects as you have memory for. This type assumes single-threaded access.

## Topics

### Creating an assignable document
- [init(pdfURL: URL, authors: [some UserIdentity], id: String?) throws](assignabledocument/init(pdfurl:authors:id:).md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.
- [init(pdfURL: URL, id: String?) throws](assignabledocument/init(pdfurl:id:).md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.
### Inspecting an assignable document
- [AssignableDocument.ID](assignabledocument/id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignableDocument.ID](assignabledocument/id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](assignabledocument/ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](assignabledocument/ispartial.md)
  Denotes whether or not this document is a partial one.
- [AssignableDocument.PartIDs](assignabledocument/partids-swift.enum.md)
  An enumeration containing the identities of parts managed by this view.
- [var partIDs: [AssignableDocument.PartID]](assignabledocument/partids-swift.property.md)
  Returns a collection of identifiers reflecting the manifest of parts available in the document.
- [AssignableDocument.Question](assignabledocument/question.md)
  A question in the assignable document.
- [AssignableDocument.QuestionBox](assignabledocument/questionbox.md)
  A box on a page for a question.
- [var questions: [AssignableDocument.Question]](assignabledocument/questions.md)
  A collection of questions defined for this assignable.
- [AssignableDocument.Element](assignabledocument/element.md)
  The type for elements of this document. An element is a component of the document such as a page or question.
- [AssignableDocument.Error](assignabledocument/error.md)
  Errors for this document type.
### Getting and setting the questions
- [func appendQuestion(pageID: AssignableDocument.Page.ID, rect: CGRect, maxScore: Double?) -> AssignableDocument.Question.ID](assignabledocument/appendquestion(pageid:rect:maxscore:).md)
  Creates a new question and appends it to the document.
- [func questions(on: AssignableDocument.Page.ID) -> [AssignableDocument.Question]](assignabledocument/questions(on:).md)
  Find questions that exist on the specified page.
- [func removeQuestion(AssignableDocument.Question.ID) -> AssignableDocument.Question?](assignabledocument/removequestion(_:).md)
  Removes a question and its boxes from the document.
### Computing the max score
- [func computeMaxScore(defaultQuestionMaxScore: Double?) -> Double?](assignabledocument/computemaxscore(defaultquestionmaxscore:).md)
  Computes the maximum possible score for this `AssignableDocument` as defined by each individual question’s `maxScore`.
### Getting the authors
- [var authors: [AnyUserIdentity]](assignabledocument/authors.md)
  The set of identities of users that created or modified this assignable. Treated as a set.
### Getting the configuration
- [AssignableDocument.Configuration](assignabledocument/configuration-swift.typealias.md)
  The configuration for an assessment which contains options for display of marks and their point values.
- [var configuration: some AssignableDocumentConfiguration](assignabledocument/configuration-swift.property.md)
  The configuration of this assessment which contains options for display of marks and their point values.
- [AssignableDocument.CorrectMarkType](assignabledocument/correctmarktype.md)
  The glyph to use that represents a correct mark.
### Merging the parts
- [func merge(other: AssignableDocument) throws -> Bool](assignabledocument/merge(other:).md)
  Merge another object of this type into this object.
### Producing thumbnails
- [func questionThumbnails(visibleParts: [AssignableDocument.PartID]) async -> [AssignableDocument.Question.ID : [AssignableDocument.Question.Thumbnail]]](assignabledocument/questionthumbnails(visibleparts:).md)
  Produces thumbnails of question regions within the document.
### Exporting the parts
- [func export(partIDs: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : URL]](assignabledocument/export(partids:).md)
  Given a set of part identifiers, return a dictionary of part ID to data objects for the requested layers.
- [func exportBaseAsPDF() async -> PDFDocument](assignabledocument/exportbaseaspdf.md)
  Exports the base part of this document to a `PDFDocument`.
### Comparing assignable documents
- [static func == (AssignableDocument, AssignableDocument) -> Bool](assignabledocument/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Hashing the assignable document
- [func hash(into: inout Hasher)](assignabledocument/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Accessing documents
- [subscript(AssignableDocument.QuestionBox.ID) -> AssignableDocument.QuestionBox?](assignabledocument/subscript(_:)-68enn.md)
  Access the question box that the identifier denotes, if any.
- [subscript(AssignableDocument.Question.ID) -> AssignableDocument.Question?](assignabledocument/subscript(_:)-7fijz.md)
  Access the question that the identifier denotes, if any.
- [subscript(AssignableDocument.Page.ID) -> AssignableDocument.Page?](assignabledocument/subscript(_:)-8ou91.md)
  Access the page that the identifier denotes, if any.
### Initializers
- [init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : URL]) throws](assignabledocument/init(id:partdata:)-4am19.md)
  Construct an instance of this object with the parts data passed in.
- [init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : MergeablePartData]) async throws](assignabledocument/init(id:partdata:)-8gf6g.md)
  Construct an instance of this object with the parts data passed in.
### Instance Properties
- [var hashValue: Int](assignabledocument/hashvalue.md)
  The hash value.
- [var pagesDebugDescription: String](assignabledocument/pagesdebugdescription.md)
### Instance Methods
- [func exportParts(identifiedBy: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : MergeablePartData]](assignabledocument/exportparts(identifiedby:).md)
  Given a set of part identifiers, return a dictionary of part ID to part data.
- [func makePart(for: AssignableDocument.PartID) throws -> MergeablePartData?](assignabledocument/makepart(for:).md)
  Creates data for the part with the given identifier.
- [func merge(AssignableDocument) async throws -> Bool](assignabledocument/merge(_:).md)
  Merge another object of this type into this object.
- [func merge(partData: MergeablePartData, into: AssignableDocument.PartID) async throws -> Bool](assignabledocument/merge(partdata:into:).md)
  Merges an individual part into the specified part of this object.
- [func merge(partID: AssignableDocument.PartID, partDataURL: URL) throws -> Bool](assignabledocument/merge(partid:partdataurl:).md)
  Merges an individual part’s data into the specified part of this object.
### Default Implementations
- [Assignable Implementations](assignabledocument/assignable-implementations.md)
- [Equatable Implementations](assignabledocument/equatable-implementations.md)
- [MergeableDocument Implementations](assignabledocument/mergeabledocument-implementations.md)

## Relationships

### Conforms To
- [Assignable](assignable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MergeableDocument](mergeabledocument.md)
- [MergeablePartsContainer](mergeablepartscontainer.md)

## See Also

- [struct AssignedWorkDocument](assignedworkdocument.md)
  An assigned work document is a document that contains taker and scorer markup specific to a taker. It also contains a copy of the assignable document upon which it is based.
- [protocol Assignable](assignable.md)
  Documents conforming to this protocol can be assigned to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument)*