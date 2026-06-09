# DiskImage.CreationConfiguration

**Framework**: DiskImageKit  
**Kind**: protocol

A marker protocol for disk image creation configurations.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol CreationConfiguration
```

## Topics

### Type Methods
- [static func asif(url: URL, blockCount: Int, blockSize: DiskImage.BlockSize) -> Self](diskimage/creationconfiguration/asif(url:blockcount:blocksize:).md)
  Returns an Apple sparse image format (ASIF) configuration for standalone or base images.
- [static func asifLayer(url: URL, type: DiskImage.LayerType) -> Self](diskimage/creationconfiguration/asiflayer(url:type:).md)
  Returns an Apple sparse image format (ASIF) configuration for stackable layers.
- [static func raw(url: URL, blockCount: Int) -> Self](diskimage/creationconfiguration/raw(url:blockcount:).md)
  Returns a RAW configuration for standalone or base images.

## Relationships

### Conforming Types
- [ASIFCreationConfiguration](asifcreationconfiguration.md)
- [ASIFLayerCreationConfiguration](asiflayercreationconfiguration.md)
- [RAWCreationConfiguration](rawcreationconfiguration.md)

## See Also

- [convenience init(creating: some DiskImage.CreationConfiguration) throws](diskimage/init(creating:).md)
  Creates a new, empty disk image.
- [struct ASIFCreationConfiguration](asifcreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk images.
- [struct ASIFLayerCreationConfiguration](asiflayercreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk image layers in stacked images.
- [struct RAWCreationConfiguration](rawcreationconfiguration.md)
  The configuration to use to create RAW disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/creationconfiguration)*