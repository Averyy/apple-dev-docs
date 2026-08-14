# NSPDFInfo

**Framework**: AppKit  
**Kind**: class

An object that stores information associated with the creation of a PDF file, such as its URL, tag names, page orientation, and paper size.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class NSPDFInfo
```

#### Overview

Typically, a PDF panel—that is, a panel created by an [`NSPDFPanel`](nspdfpanel.md) object—displays the information supplied by an [`NSPDFInfo`](nspdfinfo.md) object when the user wants to export content as a PDF file. A PDF panel can also update a PDF info object with information it receives from the user.

## Topics

### Specifying PDF Information
- [var url: URL?](nspdfinfo/url.md)
  The URL identifying the location at which the PDF file will be created.
- [var isFileExtensionHidden: Bool](nspdfinfo/isfileextensionhidden.md)
  A Boolean value that indicates whether the file extension should appear after the filename.
- [var tagNames: [String]](nspdfinfo/tagnames.md)
  An array of tag names that should be applied to the PDF file after it’s created.
- [var orientation: NSPrintInfo.PaperOrientation](nspdfinfo/orientation.md)
  The paper orientation to use when exporting content as a PDF file.
- [var paperSize: NSSize](nspdfinfo/papersize.md)
  The paper size to use when exporting content as a PDF file.
- [var attributes: NSMutableDictionary](nspdfinfo/attributes.md)
  A dictionary of additional attributes that describe how to export content as a PDF file.
### Initializers
- [init?(coder: NSCoder)](nspdfinfo/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSPDFImageRep](nspdfimagerep.md)
  An object that can render an image from a PDF format data stream.
- [class NSEPSImageRep](nsepsimagerep.md)
  An object that can render an image from encapsulated PostScript (EPS) code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfinfo)*