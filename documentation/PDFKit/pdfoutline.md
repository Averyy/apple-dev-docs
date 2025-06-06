# PDFOutline

**Framework**: PDFKit  
**Kind**: class

A `PDFOutline` object is an element in a tree-structured hierarchy that can represent the structure of a PDF document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFOutline
```

#### Overview

An outline is an optional component of a PDF document, useful for viewing the structure of the document and for navigating within it.

Outlines are created by the document’s author. If you represent a PDF document outline using outline objects, the root of the hierarchy is obtained from the PDF document itself. This root outline is not visible and serves merely as a container for the visible outlines.

## Topics

### Initializing an Outline
- [init()](pdfoutline/init.md)
  Initializes a `PDFOutline` object.
### Getting Information About an Outline
- [var document: PDFDocument?](pdfoutline/document.md)
  Returns the document with which the outline is associated.
- [var numberOfChildren: Int](pdfoutline/numberofchildren.md)
  Returns the number of child outline objects in the outline.
- [var parent: PDFOutline?](pdfoutline/parent.md)
  Returns the parent outline object of the outline (returns `NULL` if called on the root outline object).
- [func child(at: Int) -> PDFOutline?](pdfoutline/child(at:).md)
  Returns the child outline object at the specified index.
- [var index: Int](pdfoutline/index.md)
  Returns the index of the outline.
### Managing Outline Labels
- [var label: String?](pdfoutline/label.md)
  Returns the label for the outline.
### Managing Actions and Destinations
- [var destination: PDFDestination?](pdfoutline/destination.md)
  Returns the destination associated with the outline.
- [var action: PDFAction?](pdfoutline/action.md)
  Returns the action performed when users click the outline.
### Changing an Outline Hierarchy
- [func insertChild(PDFOutline, at: Int)](pdfoutline/insertchild(_:at:).md)
  Inserts the specified outline object at the specified index.
- [func removeFromParent()](pdfoutline/removefromparent.md)
  Removes the outline object from its parent (does nothing if outline object is the root outline object).
### Managing the Disclosure of an Outline Object
- [var isOpen: Bool](pdfoutline/isopen.md)
  Returns a Boolean value that indicates whether the outline object is initially disclosed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PDFDocument](pdfdocument.md)
  An object that represents PDF data or a PDF file and defines methods for writing, searching, and selecting PDF data.
- [class PDFPage](pdfpage.md)
  `PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.
- [class PDFSelection](pdfselection.md)
  A `PDFSelection` object identifies a contiguous or noncontiguous selection of text in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline)*