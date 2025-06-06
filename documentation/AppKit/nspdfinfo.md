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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPDFImageRep](nspdfimagerep.md)
  An object that can render an image from a PDF format data stream.
- [class NSEPSImageRep](nsepsimagerep.md)
  An object that can render an image from encapsulated PostScript (EPS) code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfinfo)*