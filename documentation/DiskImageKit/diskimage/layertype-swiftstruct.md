# DiskImage.LayerType

**Framework**: DiskImageKit  
**Kind**: struct

An enumeration that defines the type of a layer in a stacked disk image.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct LayerType
```

## Topics

### Operators
- [static func == (DiskImage.LayerType, DiskImage.LayerType) -> Bool](diskimage/layertype-swift.struct/==(_:_:).md)
  Equatable implementation.
### Type Properties
- [static let cache: DiskImage.LayerType](diskimage/layertype-swift.struct/cache.md)
  A cache layer.
- [static let overlay: DiskImage.LayerType](diskimage/layertype-swift.struct/overlay.md)
  An overlay layer that inherits its size from the layer beneath it.
### Type Methods
- [static func overlay(blockCount: Int) -> DiskImage.LayerType](diskimage/layertype-swift.struct/overlay(blockcount:).md)
  An overlay layer with a specific block count.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [DiskImage.Format](diskimage/format-swift.enum.md)
  Values that describe the disk image formats DiskImageKit supports.
- [DiskImage.BlockSize](diskimage/blocksize-swift.enum.md)
  Values that represent the block size of a disk image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.struct)*