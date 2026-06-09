# init(creating:)

**Framework**: DiskImageKit  
**Kind**: init

Creates a new, empty disk image.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
convenience init(creating configuration: some DiskImage.CreationConfiguration) throws
```

#### Discussion

Use this initializer to create a new standalone disk image or a base image for a stacked disk image. The `configuration` must not be a [`DiskImage.StackableLayer`](diskimage/stackablelayer.md); use [`appending(_:)`](diskimage/appending(_:)-3pfqg.md) instead.

The following example creates an ASIF disk image at a specific location, a block count, and block size you specify with an [`ASIFCreationConfiguration`](asifcreationconfiguration.md) configuration object.

```None
let image = try DiskImage(creating: .asif(url: imageURL, blockCount: 1000000000, blockSize: .bytes512))
```

> **Note**: [`InvalidBlockCountError`](invalidblockcounterror.md) if the block count is zero or negative. `POSIXError` if the disk image cannot be created.

## Parameters

- `configuration`: A configuration object that specifies the parameters for the new disk image. If the URL points to an existing file, the framework overwrites it.

## See Also

- [struct ASIFCreationConfiguration](asifcreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk images.
- [struct ASIFLayerCreationConfiguration](asiflayercreationconfiguration.md)
  The configuration to use to create Apple sparse image format (ASIF) disk image layers in stacked images.
- [DiskImage.CreationConfiguration](diskimage/creationconfiguration.md)
  A marker protocol for disk image creation configurations.
- [struct RAWCreationConfiguration](rawcreationconfiguration.md)
  The configuration to use to create RAW disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/init(creating:))*