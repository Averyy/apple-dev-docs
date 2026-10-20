# DiskImage.LayerType

**Framework**: DiskImageKit  
**Kind**: struct  
**Role**: Structure

An enumeration that defines the type of a layer in a stacked disk image.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct LayerType
```

## Topics

### Operators
- [static func == (DiskImage.LayerType, DiskImage.LayerType) -> Bool](./layertype-swift.struct/eqeq%28_,_%29.md)
  Equatable implementation.
### Type Properties
- [static let cache: DiskImage.LayerType](./layertype-swift.struct/cache.md)
  A cache layer.
- [static let overlay: DiskImage.LayerType](./layertype-swift.struct/overlay.md)
  An overlay layer that inherits its size from the layer beneath it.
### Type Methods
- [static func overlay(blockCount: Int) -> DiskImage.LayerType](./layertype-swift.struct/overlay%28blockcount%29.md)
  An overlay layer with a specific block count.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Values that describe block sizes and image formats
- [DiskImage.Format](./format-swift.enum.md)
  Values that describe the disk image formats DiskImageKit supports.
- [DiskImage.BlockSize](./blocksize-swift.enum.md)
  Values that represent the block size of a disk image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.struct)*