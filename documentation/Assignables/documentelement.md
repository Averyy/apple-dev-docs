# DocumentElement

**Framework**: Assignables  
**Kind**: protocol  
**Role**: Protocol

Represents an element that is contained within a document. Such elements can have identifiers that uniquely identify them within a document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
protocol DocumentElement : Hashable
```

## Topics

### Implementing a document element
- [associatedtype Document : MergeableDocument](./documentelement/document.md)
  The document type this element is for.

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
### Inherited By
- [AssignableDocumentElement](./assignabledocumentelement.md)
- [AssignedWorkDocumentElement](./assignedworkdocumentelement.md)
### Conforming Types
- [AssignableDocument.Page](./assignabledocument/page.md)
- [AssignableDocument.Question](./assignabledocument/question.md)
- [AssignableDocument.QuestionBox](./assignabledocument/questionbox.md)
- [AssignedWorkDocument.Page](./assignedworkdocument/page.md)
- [AssignedWorkDocument.ScoreAnnotation](./assignedworkdocument/scoreannotation.md)

## See Also

### Document elements
- [struct BasicDocumentElementID](./basicdocumentelementid.md)
  A default implementation for a document element identifier.
- [protocol DocumentElementID](./documentelementid.md)
  An identifier for an element in a document.
- [protocol AssignableDocumentElement](./assignabledocumentelement.md)
  An element of an [`AssignableDocument`](./assignabledocument.md).
- [protocol AssignedWorkDocumentElement](./assignedworkdocumentelement.md)
  An element of an [`AssignedWorkDocument`](./assignedworkdocument.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/documentelement)*