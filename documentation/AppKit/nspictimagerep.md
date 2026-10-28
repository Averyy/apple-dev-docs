# NSPICTImageRep

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that renders an image from a PICT format data stream of version 1, version 2, and extended version 2.

**Availability**:
- macOS

## Declaration

```swift
class NSPICTImageRep
```

```objc
@interface NSPICTImageRep : NSImageRep
```

## Overview

> ⚠️ **Warning**:  There is no guarantee that the image will render exactly the same as it would under QuickDraw because of the differences between the display medium and QuickDraw. In particular, some transfer modes and region operations may not be supported.

## Topics

### Creating Representations of Images from PICT Data
- [init?(data: Data)](./nspictimagerep/init%28data%29.md)
  Returns a representation of an image from the specified data in the PICT file format.
- [+ imageRepWithData:](./nspictimagerep/imagerepwithdata_.md)
  Creates and returns a representation of an image from the specified data in the PICT file format.
### Getting Data
- [var boundingBox: NSRect](./nspictimagerep/boundingbox.md)
  The rectangle that bounds the image representation.
- [var pictRepresentation: Data](./nspictimagerep/pictrepresentation.md)
  The image representation’s PICT data.

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

### Bitmap Formats
- [class NSBitmapImageRep](./nsbitmapimagerep.md)
  An object that renders an image from bitmap data.
- [class NSCIImageRep](./nsciimagerep.md)
  An object that can render an image from a Core Image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictimagerep)*