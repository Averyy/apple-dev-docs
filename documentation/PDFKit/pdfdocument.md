# PDFDocument

**Framework**: PDFKit  
**Kind**: class

An object that represents PDF data or a PDF file and defines methods for writing, searching, and selecting PDF data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFDocument
```

## Mentions

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)

#### Overview

The other utility classes are either instantiated from methods in `PDFDocument`, as are `PDFPage` and `PDFOutline`; or support it, as do `PDFSelection` and `PDFDestination`.

You initialize a `PDFDocument` object with PDF data or with a URL to a PDF file. You can then ask for the page count, add or delete pages, perform a find, or parse selected content into an `NSString` object.

## Topics

### Initializing Documents
- [init?(url: URL)](pdfdocument/init(url:).md)
  Initializes a `PDFDocument` object with the contents at the specified URL (if the URL is invalid, this method returns `NULL`).
- [init?(data: Data)](pdfdocument/init(data:).md)
  Initializes a `PDFDocument` object with the passed-in data.
- [init()](pdfdocument/init.md)
  Initializes a `PDFDocument` object.
### Reading and Writing PDFs
- [Read Operations](read-operations.md)
  Operations that let you access documents and pages, manage document security, and work with searching and selections.
- [Write Operations](write-operations.md)
  Operations that let you write document data to different locations.
### Setting the Delegate
- [var delegate: (any PDFDocumentDelegate)?](pdfdocument/delegate.md)
  The object acting as the delegate for the `PDFDocument` object.
- [protocol PDFDocumentDelegate](pdfdocumentdelegate.md)
  The delegate for the `PDFDocument` object.
### Constants
- [enum PDFDocumentPermissions](pdfdocumentpermissions.md)
  An enumeration that specifies document permissions status.
- [struct PDFDocumentAttribute](pdfdocumentattribute.md)
  A structure that specifies document attributes.
- [struct PDFDocumentWriteOption](pdfdocumentwriteoption.md)
  A structure that specifies file writing options for a document.
### Instance Properties
- [var accessPermissions: PDFAccessPermissions](pdfdocument/accesspermissions.md)
### Instance Methods
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint, with: PDFSelectionGranularity) -> PDFSelection?](pdfdocument/selection(from:at:to:at:with:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PDFPage](pdfpage.md)
  `PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.
- [class PDFOutline](pdfoutline.md)
  A `PDFOutline` object is an element in a tree-structured hierarchy that can represent the structure of a PDF document.
- [class PDFSelection](pdfselection.md)
  A `PDFSelection` object identifies a contiguous or noncontiguous selection of text in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument)*