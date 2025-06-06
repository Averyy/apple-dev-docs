# CGPDFDocument

**Framework**: Core Graphics  
**Kind**: class

A document that contains PDF (Portable Document Format) drawing information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGPDFDocument
```

#### Overview

PDF provides an efficient format for cross-platform exchange of documents with rich content. PDF files can contain multiple pages of images and text. A PDF document object contains all the information relating to a PDF document, including its catalog and contents.

Note that PDF documents may be encrypted, and that some operations may be restricted until a valid password is supplied—see the functions listed in [`Working with an Encrypted PDF Document`](cgpdfdocument#Working-with-an-Encrypted-PDF-Document.md).  Core Graphics also supports decrypting encrypted documents.

Core Graphics can both display and generate files that are compliant with the PDF standard.

## Topics

### Creating PDF Documents
- [init?(CGDataProvider)](cgpdfdocument/init(_:)-gbq6.md)
  Creates a Core Graphics PDF document using a data provider.
- [init?(CFURL)](cgpdfdocument/init(_:)-2gtsd.md)
  Creates a Core Graphics PDF document using data specified by a URL.
### Examining a PDF Document
- [var catalog: CGPDFDictionaryRef?](cgpdfdocument/catalog.md)
  Returns the document catalog of a Core Graphics PDF document.
- [var fileIdentifier: CGPDFArrayRef?](cgpdfdocument/fileidentifier.md)
  Gets the file identifier for a PDF document.
- [var info: CGPDFDictionaryRef?](cgpdfdocument/info.md)
  Gets the information dictionary for a PDF document.
- [var numberOfPages: Int](cgpdfdocument/numberofpages.md)
  Returns the number of pages in a PDF document.
- [func getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)](cgpdfdocument/getversion(majorversion:minorversion:).md)
  Returns the major and minor version numbers of a Core Graphics PDF document.
- [func page(at: Int) -> CGPDFPage?](cgpdfdocument/page(at:).md)
  Returns a page from a Core Graphics PDF document.
### Working with an Encrypted PDF Document
- [var isEncrypted: Bool](cgpdfdocument/isencrypted.md)
  Returns whether the specified PDF file is encrypted.
- [var allowsCopying: Bool](cgpdfdocument/allowscopying.md)
  Returns whether the specified PDF document allows copying.
- [var allowsPrinting: Bool](cgpdfdocument/allowsprinting.md)
  Returns whether a PDF document allows printing.
- [var isUnlocked: Bool](cgpdfdocument/isunlocked.md)
  Returns whether the specified PDF document is currently unlocked.
- [func unlockWithPassword(UnsafePointer<CChar>) -> Bool](cgpdfdocument/unlockwithpassword(_:).md)
  Unlocks an encrypted PDF document when a valid password is supplied.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgpdfdocument/typeid.md)
  Returns the type identifier for Core Graphics PDF documents.
### Abstract Types for PDF Document Content
- [class CGPDFPage](cgpdfpage.md)
  A type that represents a page in a PDF document.
- [CGPDFArray](cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFObject](cgpdfobject.md)
  An object representing content within a PDF document.
- [CGPDFStream](cgpdfstream.md)
  A stream or sequence of data bytes in a PDF document.
- [CGPDFString](cgpdfstring.md)
  A text string in a PDF document.
- [CGPDFScanner](cgpdfscanner.md)
  A parser object for handling content and operators in a PDF content stream.
- [CGPDFDictionary](cgpdfdictionary.md)
  A dictionary structure within a PDF document.
- [CGPDFContentStream](cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFOperatorTable](cgpdfoperatortable.md)
  A set of callback functions for operators used when scanning content in a PDF document.
### Instance Properties
- [var accessPermissions: CGPDFAccessPermissions](cgpdfdocument/accesspermissions.md)
- [var outline: CFDictionary?](cgpdfdocument/outline.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument)*