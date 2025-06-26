# AssignableDocument.PartIDs

**Framework**: Assignables  
**Kind**: enum

An enumeration containing the identities of parts managed by this view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
enum PartIDs
```

## Topics

### Layer types
- [static let all: [MergeablePartsContainerPartID]](assignabledocument/partids-swift.enum/all.md)
  All part IDs containable by this document.
- [static let authors: MergeablePartsContainerPartID](assignabledocument/partids-swift.enum/authors.md)
  The identifier for the part that stores authorship information.
- [static let base: MergeablePartsContainerPartID](assignabledocument/partids-swift.enum/base.md)
  The identifier for the part that contains the base PDF upon which this document is built.
- [static let instructionMarkup: MergeablePartsContainerPartID](assignabledocument/partids-swift.enum/instructionmarkup.md)
  The identifier for the part that stores markup intended to provide additional instructions to takers of the assignable.
- [static let questionBoxes: MergeablePartsContainerPartID](assignabledocument/partids-swift.enum/questionboxes.md)
  The identifier for the part that stores question definitions.
### Getting the document type
- [AssignableDocument.PartIDs.Document](assignabledocument/partids-swift.enum/document.md)
  The document type that this part ID is for.

## See Also

- [AssignableDocument.ID](assignabledocument/id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignableDocument.ID](assignabledocument/id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](assignabledocument/ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](assignabledocument/ispartial.md)
  Denotes whether or not this document is a partial one.
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
- [var pagesDebugDescription: String](assignabledocument/pagesdebugdescription.md)
- [AssignableDocument.Error](assignabledocument/error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/partids-swift.enum)*