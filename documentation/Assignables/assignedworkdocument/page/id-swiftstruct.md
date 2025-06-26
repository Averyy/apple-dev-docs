# AssignedWorkDocument.Page.ID

**Framework**: Assignables  
**Kind**: struct

A type representing the stable identity of this page.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct ID
```

## Topics

### Creating a page identifier
- [init(from: any Decoder) throws](assignedworkdocument/page/id-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Getting the page identifier
- [var assignableDocumentPageID: AssignableDocument.Page.ID](assignedworkdocument/page/id-swift.struct/assignabledocumentpageid.md)
  The [`AssignableDocument`](assignabledocument.md)  page ID that this work page ID corresponds to.
- [AssignedWorkDocument.Page.ID.Element](assignedworkdocument/page/id-swift.struct/element.md)
  The document element type that this reference is for.
### Operators
- [static func == (AssignedWorkDocument.Page.ID, AssignedWorkDocument.Page.ID) -> Bool](assignedworkdocument/page/id-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](assignedworkdocument/page/id-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](assignedworkdocument/page/id-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](assignedworkdocument/page/id-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](assignedworkdocument/page/id-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [DocumentElementID](documentelementid.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var assignableDocumentPageID: AssignableDocument.Page.ID](assignedworkdocument/page/assignabledocumentpageid.md)
  The [`AssignableDocument`](assignabledocument.md)  page ID that this work page ID corresponds to.
- [var id: AssignedWorkDocument.Page.ID](assignedworkdocument/page/id-swift.property.md)
  The stable identity of this page.
- [AssignedWorkDocument.Page.Document](assignedworkdocument/page/document.md)
  The document type this element is for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/page/id-swift.struct)*