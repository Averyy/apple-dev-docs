# PDFDocument

**Framework**: PDFKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface PDFDocument : NSObject
```

## Mentions

- [Adding Custom Graphics to a PDF](./adding-custom-graphics-to-a-pdf.md)

#### Overview

The other utility classes are either instantiated from methods in `PDFDocument`, as are `PDFPage` and `PDFOutline`; or support it, as do `PDFSelection` and `PDFDestination`.

You initialize a `PDFDocument` object with PDF data or with a URL to a PDF file. You can then ask for the page count, add or delete pages, perform a find, or parse selected content into an `NSString` object.

## Topics

### Initializing Documents
- [init?(url: URL)](./pdfdocument/init%28url%29-98jte.md)
  Initializes a `PDFDocument` object with the contents at the specified URL (if the URL is invalid, this method returns `NULL`).
- [init?(data: Data)](./pdfdocument/init%28data%29.md)
  Initializes a `PDFDocument` object with the passed-in data.
- [init()](./pdfdocument/init%28%29.md)
  Initializes a `PDFDocument` object.
### Reading and Writing PDFs
- [Read Operations](./read-operations.md)
  Operations that let you access documents and pages, manage document security, and work with searching and selections.
- [Write Operations](./write-operations.md)
  Operations that let you write document data to different locations.
### Setting the Delegate
- [var delegate: (any PDFDocumentDelegate)?](./pdfdocument/delegate.md)
  The object acting as the delegate for the `PDFDocument` object.
- [protocol PDFDocumentDelegate](./pdfdocumentdelegate.md)
  The delegate for the `PDFDocument` object.
### Constants
- [enum PDFDocumentPermissions](./pdfdocumentpermissions.md)
  An enumeration that specifies document permissions status.
- [struct PDFDocumentAttribute](./pdfdocumentattribute.md)
  A structure that specifies document attributes.
- [struct PDFDocumentWriteOption](./pdfdocumentwriteoption.md)
  A structure that specifies file writing options for a document.
### Instance Properties
- [var accessPermissions: PDFAccessPermissions](./pdfdocument/accesspermissions.md)
### Initializers
- [init?(URL: URL)](./pdfdocument/init%28url%29-7sttu.md)
### Instance Methods
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint, with: PDFSelectionGranularity) -> PDFSelection?](./pdfdocument/selection%28from,at,to,at,with%29.md)
### Notifications
- [PDFDocumentDidUnlockNotification](./pdfdocumentdidunlocknotification.md)
  A notification that a document unlocks after a [`unlockWithPassword:`](./pdfdocument/unlock%28withpassword%29.md) message.
- [PDFDocumentDidBeginFindNotification](./pdfdocumentdidbeginfindnotification.md)
  A notification that the [`beginFindString:withOptions:`](./pdfdocument/beginfindstring%28_,withoptions%29.md) or [`findString:withOptions:`](./pdfdocument/findstring%28_,withoptions%29.md) method begins finding.
- [PDFDocumentDidEndFindNotification](./pdfdocumentdidendfindnotification.md)
  A notification that the [`beginFindString:withOptions:`](./pdfdocument/beginfindstring%28_,withoptions%29.md) or [`findString:withOptions:`](./pdfdocument/findstring%28_,withoptions%29.md) method returns.
- [PDFDocumentDidBeginPageFindNotification](./pdfdocumentdidbeginpagefindnotification.md)
  A notification that a find operation begins working on a new page of a document.
- [PDFDocumentDidEndPageFindNotification](./pdfdocumentdidendpagefindnotification.md)
  A notification that a find operation finishes working on a page in a document.
- [PDFDocumentDidFindMatchNotification](./pdfdocumentdidfindmatchnotification.md)
  A notification that a string match is found in a document.
- [PDFDocumentDidBeginWriteNotification](./pdfdocumentdidbeginwritenotification.md)
  A notification that a write operation begins working on a document.
- [PDFDocumentDidEndWriteNotification](./pdfdocumentdidendwritenotification.md)
  A notification that a write operation finishes working on a document.
- [PDFDocumentDidBeginPageWriteNotification](./pdfdocumentdidbeginpagewritenotification.md)
  A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidEndPageWriteNotification](./pdfdocumentdidendpagewritenotification.md)
  A notification that a write operation finishes working on a page in a document.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Content Model
- [class PDFPage](./pdfpage.md)
  `PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.
- [class PDFOutline](./pdfoutline.md)
  A `PDFOutline` object is an element in a tree-structured hierarchy that can represent the structure of a PDF document.
- [class PDFSelection](./pdfselection.md)
  A `PDFSelection` object identifies a contiguous or noncontiguous selection of text in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument)*