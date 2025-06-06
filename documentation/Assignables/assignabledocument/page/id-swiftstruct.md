# AssignableDocument.Page.ID

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
- [init(from: any Decoder) throws](assignabledocument/page/id-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [AssignableDocument.Page.ID.Element](assignabledocument/page/id-swift.struct/element.md)
  The document element type that this reference is for.
### Operators
- [static func == (AssignableDocument.Page.ID, AssignableDocument.Page.ID) -> Bool](assignabledocument/page/id-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var debugDescription: String](assignabledocument/page/id-swift.struct/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var hashValue: Int](assignabledocument/page/id-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](assignabledocument/page/id-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](assignabledocument/page/id-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](assignabledocument/page/id-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [DocumentElementID](documentelementid.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var id: AssignableDocument.Page.ID](assignabledocument/page/id-swift.property.md)
  The stable identity of this page.
- [var size: CGSize](assignabledocument/page/size.md)
  The dimensions of the page in this document.
- [AssignableDocument.Page.Document](assignabledocument/page/document.md)
  The document type this element is for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/page/id-swift.struct)*