# AssignedWorkDocument.Page

**Framework**: Assignables  
**Kind**: struct

A page within this assigned work document.

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

### Inspecting the properties
- [var assignableDocumentPageID: AssignableDocument.Page.ID](assignedworkdocument/page/assignabledocumentpageid.md)
  The [`AssignableDocument`](assignabledocument.md)  page ID that this work page ID corresponds to.
- [AssignedWorkDocument.Page.ID](assignedworkdocument/page/id-swift.struct.md)
  A type representing the stable identity of this page.
- [var id: AssignedWorkDocument.Page.ID](assignedworkdocument/page/id-swift.property.md)
  The stable identity of this page.
- [AssignedWorkDocument.Page.Document](assignedworkdocument/page/document.md)
  The document type this element is for.
### Hashing the page
- [func hash(into: inout Hasher)](assignedworkdocument/page/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing pages
- [static func == (AssignedWorkDocument.Page, AssignedWorkDocument.Page) -> Bool](assignedworkdocument/page/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var debugDescription: String](assignedworkdocument/page/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var hashValue: Int](assignedworkdocument/page/hashvalue.md)
  The hash value.
- [var rotation: Measurement<UnitAngle>](assignedworkdocument/page/rotation.md)
  The rotation of the page in this document.
### Default Implementations
- [Equatable Implementations](assignedworkdocument/page/equatable-implementations.md)

## Relationships

### Conforms To
- [AssignedWorkDocumentElement](assignedworkdocumentelement.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [DocumentElement](documentelement.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MergeableDocumentPage](mergeabledocumentpage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/page)*