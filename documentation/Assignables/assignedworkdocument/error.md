# AssignedWorkDocument.Error

**Framework**: Assignables  
**Kind**: enum

Errors for this document type.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
enum Error
```

## Topics

### Variant error
- [AssignedWorkDocument.Error.otherDocumentIsNotAVariant](assignedworkdocument/error/otherdocumentisnotavariant.md)
  The other document to be merged into the current document is not a variant of the current document, so merge isn’t possible.
### Enumeration Cases
- [case exportFailed(partIDs: [AssignedWorkDocument.PartID])](assignedworkdocument/error/exportfailed(partids:).md)
  Export of data from the document failed.
### Default Implementations
- [Error Implementations](assignedworkdocument/error/error-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/error)*