# AssignedWorkDocument.PartIDs

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
- [static let all: [MergeablePartsContainerPartID]](assignedworkdocument/partids-swift.enum/all.md)
  All part IDs containable by this document.
- [static let assignableDocumentAuthors: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/assignabledocumentauthors.md)
  The identifier for the part that stores authorship information.
- [static let assignableDocumentBase: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/assignabledocumentbase.md)
  The identifier for the part that contains the base PDF upon which this document is built.
- [static let assignableDocumentInstructionMarkup: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/assignabledocumentinstructionmarkup.md)
  The identifier for the part that stores markup intended to provide additional instructions to takers of the assignable.
- [static let assignableDocumentQuestionBoxes: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/assignabledocumentquestionboxes.md)
  The identifier for the part that stores question definitions.
- [static let assignees: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/assignees.md)
  The identifier for the part that stores takers participating in this document.
- [static let scoreAnnotations: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/scoreannotations.md)
  The identifier for the part that stores score annotations.
- [static let scorerMarkup: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/scorermarkup.md)
  The identifier for the part that stores markup created by the scorer.
- [static let scorers: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/scorers.md)
  The identifier for the part that stores scorers participating in grading this document.
- [static let takerMarkup: MergeablePartsContainerPartID](assignedworkdocument/partids-swift.enum/takermarkup.md)
  The identifier for the part that stores markup created by the taker.
### Getting the document type
- [AssignedWorkDocument.PartIDs.Document](assignedworkdocument/partids-swift.enum/document.md)
  The document type that this part ID is for.

## See Also

- [AssignedWorkDocument.ID](assignedworkdocument/id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignedWorkDocument.ID](assignedworkdocument/id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](assignedworkdocument/ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](assignedworkdocument/ispartial.md)
  Denotes whether or not this document is a partial one.
- [var partIDs: [MergeablePartsContainerPartID]](assignedworkdocument/partids-swift.property.md)
  Returns a collection of identifiers reflecting the manifest of parts available in the document.
- [var scoreAnnotations: [AssignedWorkDocument.ScoreAnnotation]](assignedworkdocument/scoreannotations.md)
  The collection of score annotations for this work document. Treated as a multiset. i.e. The order of the elements doesn’t matter and duplicate values are allowed.
- [var scorers: [AnyUserIdentity]](assignedworkdocument/scorers.md)
  The identities of users scoring this assigned work. Treated as a set.
- [var pagesDebugDescription: String](assignedworkdocument/pagesdebugdescription.md)
- [AssignedWorkDocument.Error](assignedworkdocument/error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/partids-swift.enum)*