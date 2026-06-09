# ASIFLayerCreationConfiguration

**Framework**: DiskImageKit  
**Kind**: struct

The configuration to use to create Apple sparse image format (ASIF) disk image layers in stacked images.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct ASIFLayerCreationConfiguration
```

#### Overview

This type is returned by `asifLayer(url:type:)` and can only be used with stacking operations like `DiskImage/appending(_:)-(CreationConfiguration&StackableLayer)`.

## Relationships

### Conforms To
- [DiskImage.CreationConfiguration](diskimage/creationconfiguration.md)
- [DiskImage.StackableLayer](diskimage/stackablelayer.md)

## See Also

- [convenience init(creating: some DiskImage.CreationConfiguration) throws](diskimage/init(creating:).md)
  Creates a new, empty disk image.
- [struct ASIFCreationConfiguration](asifcreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk images.
- [DiskImage.CreationConfiguration](diskimage/creationconfiguration.md)
  A marker protocol for disk image creation configurations.
- [struct RAWCreationConfiguration](rawcreationconfiguration.md)
  The configuration to use to create RAW disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/asiflayercreationconfiguration)*