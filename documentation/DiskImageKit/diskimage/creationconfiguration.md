# DiskImage.CreationConfiguration

**Framework**: DiskImageKit  
**Kind**: protocol  
**Role**: Protocol

A marker protocol for disk image creation configurations.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol CreationConfiguration
```

## Topics

### Type Methods
- [static func asif(url: URL, blockCount: Int, blockSize: DiskImage.BlockSize) -> Self](./creationconfiguration/asif%28url,blockcount,blocksize%29.md)
  Returns an Apple sparse image format (ASIF) configuration for standalone or base images.
- [static func asifLayer(url: URL, type: DiskImage.LayerType) -> Self](./creationconfiguration/asiflayer%28url,type%29.md)
  Returns an Apple sparse image format (ASIF) configuration for stackable layers.
- [static func raw(url: URL, blockCount: Int) -> Self](./creationconfiguration/raw%28url,blockcount%29.md)
  Returns a RAW configuration for standalone or base images.

## Relationships

### Conforming Types
- [ASIFCreationConfiguration](../asifcreationconfiguration.md)
- [ASIFLayerCreationConfiguration](../asiflayercreationconfiguration.md)
- [RAWCreationConfiguration](../rawcreationconfiguration.md)

## See Also

### Creating disk images
- [convenience init(creating: some DiskImage.CreationConfiguration) throws](./init%28creating%29.md)
  Creates a new, empty disk image.
- [struct ASIFCreationConfiguration](../asifcreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk images.
- [struct ASIFLayerCreationConfiguration](../asiflayercreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk image layers in stacked images.
- [struct RAWCreationConfiguration](../rawcreationconfiguration.md)
  The configuration to use to create RAW disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/creationconfiguration)*