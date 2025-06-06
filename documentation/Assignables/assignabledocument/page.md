# AssignableDocument.Page

**Framework**: Assignables  
**Kind**: struct

A page within this assignable document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct Page
```

## Topics

### Inspecting a page
- [AssignableDocument.Page.ID](assignabledocument/page/id-swift.struct.md)
  A type representing the stable identity of this page.
- [var id: AssignableDocument.Page.ID](assignabledocument/page/id-swift.property.md)
  The stable identity of this page.
- [var size: CGSize](assignabledocument/page/size.md)
  The dimensions of the page in this document.
- [AssignableDocument.Page.Document](assignabledocument/page/document.md)
  The document type this element is for.
### Comparing pages
- [static func == (AssignableDocument.Page, AssignableDocument.Page) -> Bool](assignabledocument/page/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Hashing a page
- [func hash(into: inout Hasher)](assignabledocument/page/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Instance Properties
- [var debugDescription: String](assignabledocument/page/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var hashValue: Int](assignabledocument/page/hashvalue.md)
  The hash value.
- [var rotation: Measurement<UnitAngle>](assignabledocument/page/rotation.md)
  The rotation of the page in this document.
### Default Implementations
- [Equatable Implementations](assignabledocument/page/equatable-implementations.md)

## Relationships

### Conforms To
- [AssignableDocumentElement](assignabledocumentelement.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [DocumentElement](documentelement.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MergeableDocumentPage](mergeabledocumentpage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/page)*