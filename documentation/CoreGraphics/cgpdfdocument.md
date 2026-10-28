# CGPDFDocument

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A document that contains PDF (Portable Document Format) drawing information.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CGPDFDocument
```

```c
typedef struct CGPDFDocument * CGPDFDocumentRef;
```

## Overview

PDF provides an efficient format for cross-platform exchange of documents with rich content. PDF files can contain multiple pages of images and text. A PDF document object contains all the information relating to a PDF document, including its catalog and contents.

Note that PDF documents may be encrypted, and that some operations may be restricted until a valid password is supplied—see the functions listed in [Working with an Encrypted PDF Document](./cgpdfdocument.md#Working-with-an-Encrypted-PDF-Document).  Core Graphics also supports decrypting encrypted documents.

Core Graphics can both display and generate files that are compliant with the PDF standard.

## Topics

### Creating PDF Documents
- [init?(CGDataProvider)](./cgpdfdocument/init%28_%29-gbq6.md)
  Creates a Core Graphics PDF document using a data provider.
- [init?(CFURL)](./cgpdfdocument/init%28_%29-2gtsd.md)
  Creates a Core Graphics PDF document using data specified by a URL.
### Examining a PDF Document
- [var catalog: CGPDFDictionaryRef?](./cgpdfdocument/catalog.md)
  Returns the document catalog of a Core Graphics PDF document.
- [var fileIdentifier: CGPDFArrayRef?](./cgpdfdocument/fileidentifier.md)
  Gets the file identifier for a PDF document.
- [var info: CGPDFDictionaryRef?](./cgpdfdocument/info.md)
  Gets the information dictionary for a PDF document.
- [var numberOfPages: Int](./cgpdfdocument/numberofpages.md)
  Returns the number of pages in a PDF document.
- [func getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)](./cgpdfdocument/getversion%28majorversion,minorversion%29.md)
  Returns the major and minor version numbers of a Core Graphics PDF document.
- [func page(at: Int) -> CGPDFPage?](./cgpdfdocument/page%28at%29.md)
  Returns a page from a Core Graphics PDF document.
### Working with an Encrypted PDF Document
- [var isEncrypted: Bool](./cgpdfdocument/isencrypted.md)
  Returns whether the specified PDF file is encrypted.
- [var allowsCopying: Bool](./cgpdfdocument/allowscopying.md)
  Returns whether the specified PDF document allows copying.
- [var allowsPrinting: Bool](./cgpdfdocument/allowsprinting.md)
  Returns whether a PDF document allows printing.
- [var isUnlocked: Bool](./cgpdfdocument/isunlocked.md)
  Returns whether the specified PDF document is currently unlocked.
- [func unlockWithPassword(UnsafePointer<CChar>) -> Bool](./cgpdfdocument/unlockwithpassword%28_%29.md)
  Unlocks an encrypted PDF document when a valid password is supplied.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgpdfdocument/typeid.md)
  Returns the type identifier for Core Graphics PDF documents.
### Abstract Types for PDF Document Content
- [class CGPDFPage](./cgpdfpage.md)
  A type that represents a page in a PDF document.
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFObject](./cgpdfobject.md)
  An object representing content within a PDF document.
- [CGPDFStream](./cgpdfstream.md)
  A stream or sequence of data bytes in a PDF document.
- [CGPDFString](./cgpdfstring.md)
  A text string in a PDF document.
- [CGPDFScanner](./cgpdfscanner.md)
  A parser object for handling content and operators in a PDF content stream.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFOperatorTable](./cgpdfoperatortable.md)
  A set of callback functions for operators used when scanning content in a PDF document.
### Instance Properties
- [var accessPermissions: CGPDFAccessPermissions](./cgpdfdocument/accesspermissions.md)
- [var outline: CFDictionary?](./cgpdfdocument/outline.md)
### Retaining and Releasing PDF Documents
- [CGPDFDocumentRelease](./cgpdfdocumentrelease.md)
  Decrements the retain count of a PDF document.
- [CGPDFDocumentRetain](./cgpdfdocumentretain.md)
  Increments the retain count of a Core Graphics PDF document.
### Getting Page Information
- [CGPDFDocumentGetArtBox](./cgpdfdocumentgetartbox.md)
  Returns the art box of a page in a PDF document.
- [CGPDFDocumentGetBleedBox](./cgpdfdocumentgetbleedbox.md)
  Returns the bleed box of a page in a PDF document.
- [CGPDFDocumentGetCropBox](./cgpdfdocumentgetcropbox.md)
  Returns the crop box of a page in a PDF document.
- [CGPDFDocumentGetMediaBox](./cgpdfdocumentgetmediabox.md)
  Returns the media box of a page in a PDF document.
- [CGPDFDocumentGetRotationAngle](./cgpdfdocumentgetrotationangle.md)
  Returns the rotation angle of a page in a PDF document.
- [CGPDFDocumentGetTrimBox](./cgpdfdocumentgettrimbox.md)
  Returns the trim box of a page in a PDF document.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [CGContextRef](./cgcontext.md)
  A Quartz 2D drawing environment.
- [CGColorRef](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfoRef](./cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpaceRef](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [CGDataConsumerRef](./cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProviderRef](./cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGFontRef](./cgfont.md)
  A set of character glyphs and layout information for drawing text.
- [CGFunctionRef](./cgfunction.md)
  A general facility for defining and using callback functions.
- [CGGradientRef](./cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGImageRef](./cgimage.md)
  A bitmap image or image mask.
- [CGLayerRef](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.
- [CGPathRef](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGPatternRef](./cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument)*