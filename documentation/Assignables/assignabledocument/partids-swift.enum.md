# AssignableDocument.PartIDs

**Framework**: Assignables  
**Kind**: enum  
**Role**: Enumeration

An enumeration containing the identities of parts managed by this view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
enum PartIDs
```

## Topics

### Layer types
- [static let all: [MergeablePartsContainerPartID]](./partids-swift.enum/all.md)
  All part IDs containable by this document.
- [static let authors: MergeablePartsContainerPartID](./partids-swift.enum/authors.md)
  The identifier for the part that stores authorship information.
- [static let base: MergeablePartsContainerPartID](./partids-swift.enum/base.md)
  The identifier for the part that contains the base PDF upon which this document is built.
- [static let instructionMarkup: MergeablePartsContainerPartID](./partids-swift.enum/instructionmarkup.md)
  The identifier for the part that stores markup intended to provide additional instructions to takers of the assignable.
- [static let questionBoxes: MergeablePartsContainerPartID](./partids-swift.enum/questionboxes.md)
  The identifier for the part that stores question definitions.
### Getting the document type
- [AssignableDocument.PartIDs.Document](./partids-swift.enum/document.md)
  The document type that this part ID is for.

## See Also

### Inspecting an assignable document
- [AssignableDocument.ID](./id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignableDocument.ID](./id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](./ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](./ispartial.md)
  Denotes whether or not this document is a partial one.
- [var partIDs: [AssignableDocument.PartID]](./partids-swift.property.md)
  Returns a collection of identifiers reflecting the manifest of parts available in the document.
- [AssignableDocument.Question](./question.md)
  A question in the assignable document.
- [AssignableDocument.QuestionBox](./questionbox.md)
  A box on a page for a question.
- [var questions: [AssignableDocument.Question]](./questions.md)
  A collection of questions defined for this assignable.
- [AssignableDocument.Element](./element.md)
  The type for elements of this document. An element is a component of the document such as a page or question.
- [var pagesDebugDescription: String](./pagesdebugdescription.md)
- [AssignableDocument.Error](./error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/partids-swift.enum)*