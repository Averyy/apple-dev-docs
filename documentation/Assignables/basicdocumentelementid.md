# BasicDocumentElementID

**Framework**: Assignables  
**Kind**: struct

A default implementation for a document element identifier.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct BasicDocumentElementID<Element> where Element : DocumentElement
```

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [DocumentElementID](documentelementid.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [protocol DocumentElement](documentelement.md)
  Represents an element that is contained within a document. Such elements can have identifiers that uniquely identify them within a document.
- [protocol DocumentElementID](documentelementid.md)
  An identifier for an element in a document.
- [protocol AssignableDocumentElement](assignabledocumentelement.md)
  An element of an [`AssignableDocument`](assignabledocument.md).
- [protocol AssignedWorkDocumentElement](assignedworkdocumentelement.md)
  An element of an [`AssignedWorkDocument`](assignedworkdocument.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/basicdocumentelementid)*