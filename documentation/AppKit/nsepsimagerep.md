# NSEPSImageRep

**Framework**: AppKit  
**Kind**: class

An object that can render an image from encapsulated PostScript (EPS) code.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSEPSImageRep
```

## Topics

### Creating Representations of Images from EPS Data
- [init?(data: Data)](nsepsimagerep/init(data:).md)
  Returns a representation of an image initialized with the specified EPS data.
### Getting Data
- [var boundingBox: NSRect](nsepsimagerep/boundingbox.md)
  The rectangle that bounds the image representation.
- [var epsRepresentation: Data](nsepsimagerep/epsrepresentation.md)
  The EPS representation of the image representation.
### Drawing Images
- [func prepareGState()](nsepsimagerep/preparegstate.md)
  Implemented by subclasses to configure the graphics state prior to drawing.

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

- [class NSPDFImageRep](nspdfimagerep.md)
  An object that can render an image from a PDF format data stream.
- [class NSPDFInfo](nspdfinfo.md)
  An object that stores information associated with the creation of a PDF file, such as its URL, tag names, page orientation, and paper size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsepsimagerep)*