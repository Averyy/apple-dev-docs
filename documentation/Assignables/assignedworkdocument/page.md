# AssignedWorkDocument.Page

**Framework**: Assignables  
**Kind**: struct  
**Role**: Structure

A page within this assigned work document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
struct Page
```

## Topics

### Inspecting the properties
- [var assignableDocumentPageID: AssignableDocument.Page.ID](./page/assignabledocumentpageid.md)
  The [`AssignableDocument`](../assignabledocument.md)  page ID that this work page ID corresponds to.
- [AssignedWorkDocument.Page.ID](./page/id-swift.struct.md)
  A type representing the stable identity of this page.
- [var id: AssignedWorkDocument.Page.ID](./page/id-swift.property.md)
  The stable identity of this page.
- [AssignedWorkDocument.Page.Document](./page/document.md)
  The document type this element is for.
### Hashing the page
- [func hash(into: inout Hasher)](./page/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing pages
- [static func == (AssignedWorkDocument.Page, AssignedWorkDocument.Page) -> Bool](./page/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var rotation: Measurement<UnitAngle>](./page/rotation.md)
  The rotation of the page in this document.

## Relationships

### Conforms To
- [AssignedWorkDocumentElement](../assignedworkdocumentelement.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [DocumentElement](../documentelement.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [MergeableDocumentPage](../mergeabledocumentpage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/page)*