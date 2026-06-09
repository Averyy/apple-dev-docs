# DiskImage.StackableLayer

**Framework**: DiskImageKit  
**Kind**: protocol

A marker protocol that stackable disk image layer configuration objects conform to.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol StackableLayer
```

#### Overview

The [`appending(_:)`](diskimage/appending(_:)-3pfqg.md) method accepts objects that conform to this protocol.  For more information about image layering, see [`StackedImage`](stackedimage.md).

## Relationships

### Conforming Types
- [ASIFLayerCreationConfiguration](asiflayercreationconfiguration.md)

## See Also

- [func appending(consuming DiskImage) throws -> any StackedImage](diskimage/appending(_:)-4wifj.md)
  Appends a layer to this disk image, creating or extending a stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/stackablelayer)*