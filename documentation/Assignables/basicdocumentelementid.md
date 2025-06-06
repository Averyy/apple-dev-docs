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

## Topics

### Creating an element identifier
- [init(from: any Decoder) throws](basicdocumentelementid/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (BasicDocumentElementID<Element>, BasicDocumentElementID<Element>) -> Bool](basicdocumentelementid/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](basicdocumentelementid/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](basicdocumentelementid/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](basicdocumentelementid/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](basicdocumentelementid/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [DocumentElementID](documentelementid.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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