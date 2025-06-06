# NSPICTImageRep

**Framework**: AppKit  
**Kind**: class

An object that renders an image from a PICT format data stream of version 1, version 2, and extended version 2.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSPICTImageRep
```

#### Overview

> ⚠️ **Warning**:  There is no guarantee that the image will render exactly the same as it would under QuickDraw because of the differences between the display medium and QuickDraw. In particular, some transfer modes and region operations may not be supported.

 There is no guarantee that the image will render exactly the same as it would under QuickDraw because of the differences between the display medium and QuickDraw. In particular, some transfer modes and region operations may not be supported.

## Topics

### Creating Representations of Images from PICT Data
- [init?(data: Data)](nspictimagerep/init(data:).md)
  Returns a representation of an image from the specified data in the PICT file format.
### Getting Data
- [var boundingBox: NSRect](nspictimagerep/boundingbox.md)
  The rectangle that bounds the image representation.
- [var pictRepresentation: Data](nspictimagerep/pictrepresentation.md)
  The image representation’s PICT data.

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

- [class NSBitmapImageRep](nsbitmapimagerep.md)
  An object that renders an image from bitmap data.
- [class NSCIImageRep](nsciimagerep.md)
  An object that can render an image from a Core Image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictimagerep)*