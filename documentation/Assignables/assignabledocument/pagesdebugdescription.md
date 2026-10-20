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

### Inspecting an assignable document
- [AssignableDocument.ID](./id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignableDocument.ID](./id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](./ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](./ispartial.md)
  Denotes whether or not this document is a partial one.
- [AssignableDocument.PartIDs](./partids-swift.enum.md)
  An enumeration containing the identities of parts managed by this view.
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
- [AssignableDocument.Error](./error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/pagesdebugdescription)*