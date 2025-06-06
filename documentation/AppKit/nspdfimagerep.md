# NSPDFImageRep

**Framework**: AppKit  
**Kind**: class

An object that can render an image from a PDF format data stream.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSPDFImageRep
```

## Topics

### Creating Representations of Images from PDF Data
- [init?(data: Data)](nspdfimagerep/init(data:).md)
  Returns a representation of an image initialized with the specified PDF data.
### Getting Data
- [var bounds: NSRect](nspdfimagerep/bounds.md)
  The image representation’s bounding rectangle.
- [var currentPage: Int](nspdfimagerep/currentpage.md)
  The page currently displayed by the image representation.
- [var pageCount: Int](nspdfimagerep/pagecount.md)
  The number of pages in the image representation.
- [var pdfRepresentation: Data](nspdfimagerep/pdfrepresentation.md)
  The PDF representation of the representation’s image.

## Relationships

### Inherits From
- [NSImageRep](nsimagerep.md)
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

- [class NSPDFInfo](nspdfinfo.md)
  An object that stores information associated with the creation of a PDF file, such as its URL, tag names, page orientation, and paper size.
- [class NSEPSImageRep](nsepsimagerep.md)
  An object that can render an image from encapsulated PostScript (EPS) code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfimagerep)*