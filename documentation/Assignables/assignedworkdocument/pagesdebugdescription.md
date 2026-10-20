# pagesDebugDescription

**Framework**: Assignables  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
var pagesDebugDescription: String { get }
```

## See Also

### Inspecting a work document
- [AssignedWorkDocument.ID](./id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignedWorkDocument.ID](./id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](./ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](./ispartial.md)
  Denotes whether or not this document is a partial one.
- [AssignedWorkDocument.PartIDs](./partids-swift.enum.md)
  An enumeration containing the identities of parts managed by this view.
- [var partIDs: [MergeablePartsContainerPartID]](./partids-swift.property.md)
  Returns a collection of identifiers reflecting the manifest of parts available in the document.
- [var scoreAnnotations: [AssignedWorkDocument.ScoreAnnotation]](./scoreannotations.md)
  The collection of score annotations for this work document. Treated as a multiset. i.e. The order of the elements doesn’t matter and duplicate values are allowed.
- [var scorers: [AnyUserIdentity]](./scorers.md)
  The identities of users scoring this assigned work. Treated as a set.
- [AssignedWorkDocument.Error](./error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/pagesdebugdescription)*