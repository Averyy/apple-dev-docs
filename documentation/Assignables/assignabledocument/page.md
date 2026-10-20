# AssignableDocument.Page

**Framework**: Assignables  
**Kind**: struct  
**Role**: Structure

A page within this assignable document.

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

### Inspecting a page
- [AssignableDocument.Page.ID](./page/id-swift.struct.md)
  A type representing the stable identity of this page.
- [var id: AssignableDocument.Page.ID](./page/id-swift.property.md)
  The stable identity of this page.
- [var size: CGSize](./page/size.md)
  The dimensions of the page in this document.
- [AssignableDocument.Page.Document](./page/document.md)
  The document type this element is for.
### Comparing pages
- [static func == (AssignableDocument.Page, AssignableDocument.Page) -> Bool](./page/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
### Hashing a page
- [func hash(into: inout Hasher)](./page/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Instance Properties
- [var rotation: Measurement<UnitAngle>](./page/rotation.md)
  The rotation of the page in this document.

## Relationships

### Conforms To
- [AssignableDocumentElement](../assignabledocumentelement.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [DocumentElement](../documentelement.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [MergeableDocumentPage](../mergeabledocumentpage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/page)*