# DocumentElementID

**Framework**: Assignables  
**Kind**: protocol

An identifier for an element in a document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
protocol DocumentElementID : Decodable, Encodable, Hashable
```

## Topics

### Implementing an element identifier
- [associatedtype Element : DocumentElement](documentelementid/element.md)
  The document element type that this reference is for.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [AssignableDocument.Page.ID](assignabledocument/page/id-swift.struct.md)
- [AssignedWorkDocument.Page.ID](assignedworkdocument/page/id-swift.struct.md)
- [BasicDocumentElementID](basicdocumentelementid.md)

## See Also

- [protocol DocumentElement](documentelement.md)
  Represents an element that is contained within a document. Such elements can have identifiers that uniquely identify them within a document.
- [struct BasicDocumentElementID](basicdocumentelementid.md)
  A default implementation for a document element identifier.
- [protocol AssignableDocumentElement](assignabledocumentelement.md)
  An element of an [`AssignableDocument`](assignabledocument.md).
- [protocol AssignedWorkDocumentElement](assignedworkdocumentelement.md)
  An element of an [`AssignedWorkDocument`](assignedworkdocument.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/documentelementid)*