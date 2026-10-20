# partIDs

**Framework**: Assignables  
**Kind**: property

Returns a collection of identifiers reflecting the manifest of parts available in the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
var partIDs: [MergeablePartsContainerPartID] { get }
```

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
- [var scoreAnnotations: [AssignedWorkDocument.ScoreAnnotation]](assignedworkdocument/scoreannotations.md)
  The collection of score annotations for this work document. Treated as a multiset. i.e. The order of the elements doesn’t matter and duplicate values are allowed.
- [var scorers: [AnyUserIdentity]](assignedworkdocument/scorers.md)
  The identities of users scoring this assigned work. Treated as a set.
- [var pagesDebugDescription: String](assignedworkdocument/pagesdebugdescription.md)
- [AssignedWorkDocument.Error](assignedworkdocument/error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/partids-swift.property)*