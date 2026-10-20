# ASIFCreationConfiguration

**Framework**: DiskImageKit  
**Kind**: struct  
**Role**: Structure

The configuration to use to create Apple sparse image format (ASIF) disk images.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct ASIFCreationConfiguration
```

## Topics

### Type Methods
- [static func layer(url: URL, type: DiskImage.LayerType) -> ASIFLayerCreationConfiguration](./asifcreationconfiguration/layer%28url,type%29.md)
  Creates a configuration object for a new Apple sparse image format (ASIF) disk image layer.

## Relationships

### Conforms To
- [DiskImage.CreationConfiguration](./diskimage/creationconfiguration.md)

## See Also

### Creating disk images
- [convenience init(creating: some DiskImage.CreationConfiguration) throws](./diskimage/init%28creating%29.md)
  Creates a new, empty disk image.
- [struct ASIFLayerCreationConfiguration](./asiflayercreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk image layers in stacked images.
- [DiskImage.CreationConfiguration](./diskimage/creationconfiguration.md)
  A marker protocol for disk image creation configurations.
- [struct RAWCreationConfiguration](./rawcreationconfiguration.md)
  The configuration to use to create RAW disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/asifcreationconfiguration)*