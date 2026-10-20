# NSEPSImageRep

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that can render an image from encapsulated PostScript (EPS) code.

**Availability**:
- macOS 10.0+ - Deprecated in 14.0

> **Deprecated**: `NSEPSImageRep` instances cannot be created on macOS 14.0 and later

## Declaration

```swift
class NSEPSImageRep
```

```objc
@interface NSEPSImageRep : NSImageRep
```

## Topics

### Creating Representations of Images from EPS Data
- [init?(data: Data)](./nsepsimagerep/init%28data%29.md)
  Returns a representation of an image initialized with the specified EPS data.
### Getting Data
- [var boundingBox: NSRect](./nsepsimagerep/boundingbox.md)
  The rectangle that bounds the image representation.
- [var epsRepresentation: Data](./nsepsimagerep/epsrepresentation.md)
  The EPS representation of the image representation.
### Drawing Images
- [func prepareGState()](./nsepsimagerep/preparegstate%28%29.md)
  Implemented by subclasses to configure the graphics state prior to drawing.

## Relationships

### Inherits From
- [NSImageRep](./nsimagerep.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Vector Formats
- [class NSPDFImageRep](./nspdfimagerep.md)
  An object that can render an image from a PDF format data stream.
- [class NSPDFInfo](./nspdfinfo.md)
  An object that stores information associated with the creation of a PDF file, such as its URL, tag names, page orientation, and paper size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsepsimagerep)*