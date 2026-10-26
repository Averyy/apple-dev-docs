# NSCIImageRep

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that can render an image from a Core Image object.

**Availability**:
- macOS

## Declaration

```swift
class NSCIImageRep
```

```objc
@interface NSCIImageRep : NSImageRep
```

## Topics

### Creating Representations of Core Image Objects
- [init(ciImage: CIImage)](./nsciimagerep/init%28ciimage%29-60ghw.md)
  Returns a representation of an image initialized to the specified Core Image instance.
- [+ imageRepWithCIImage:](./nsciimagerep/imagerepwithciimage_.md)
  Creates and returns a representation of an image initialized to the specified Core Image instance.
### Getting Data
- [var ciImage: CIImage](./nsciimagerep/ciimage.md)
  The Core Image instance.
### Initializers
- [init(CIImage: CIImage)](./nsciimagerep/init%28ciimage%29-4wx5x.md)
- [convenience init(CIImage: CIImage)](./nsciimagerep/init%28ciimage%29-73fvp.md)

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
- [class NSPICTImageRep](./nspictimagerep.md)
  An object that renders an image from a PICT format data stream of version 1, version 2, and extended version 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsciimagerep)*