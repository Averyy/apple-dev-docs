# DiskImage

**Framework**: DiskImageKit  
**Kind**: class

The representation of an open disk image

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class DiskImage
```

#### Overview

To use a disk image as storage for virtual machine, use this object with the Virtualization API method [`init(diskImage:cachingMode:synchronizationMode:)`](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/init(diskimage:cachingmode:synchronizationmode:)). In addition, it contains properties that describe the disk image and operations to manipulate it.

An image can either be standalone or part of a stack. For more information on stacked disk image, see [`StackedImage`](stackedimage.md).

The following example demonstrates how to create a stacked disk image with 3 layers:

```None
// Open the base image.
let baseImage = try DiskImage(opening: .open(url: baseImageURL))

// Append a new cache layer,
var stackedImage = try baseImage.appending(.asifLayer(url: cacheURL, type: .cache))

// Append an existing overlay layer,
let overlayImage = try DiskImage(opening: .open(url: overlayURL))
stackedImage = try stackedImage.appending(overlayImage)

// Append a new overlay layer.
stackedImage = try stackedImage.appending(.asifLayer(url: overlayURL, type: .overlay))
```

The example demonstrates how to create a standalone, 512 GB (1 billion block) ASIF disk image:

```None
_ = try DiskImage(creating: .asif(url: imageURL, blockCount: 1000000000, blockSize: .bytes512))
```

## Topics

### Protocols
- [DiskImage.CreationConfiguration](diskimage/creationconfiguration.md)
  A marker protocol for disk image creation configurations.
- [DiskImage.StackableLayer](diskimage/stackablelayer.md)
  A marker protocol that stackable disk image layer configuration objects conform to.
### Structures
- [DiskImage.LayerType](diskimage/layertype-swift.struct.md)
  An enumeration that defines the type of a layer in a stacked disk image.
### Initializers
- [convenience init(creating: some DiskImage.CreationConfiguration) throws](diskimage/init(creating:).md)
  Creates a new, empty disk image.
- [convenience init(opening: some OpenConfigurationProtocol) throws](diskimage/init(opening:).md)
  Opens an existing disk image using the specified image URL.
### Instance Properties
- [var blockCount: Int](diskimage/blockcount.md)
  The number of blocks in the disk image.
- [var blockSize: DiskImage.BlockSize](diskimage/blocksize-swift.property.md)
  The block size, either 512 bytes or 4 KB.
- [var format: DiskImage.Format](diskimage/format-swift.property.md)
  The format of the disk image.
- [var layerType: DiskImage.LayerType?](diskimage/layertype-swift.property.md)
  The layer type of the disk image.
- [var layerUUID: UUID?](diskimage/layeruuid.md)
  A UUID of the image that the framework uses to validate its compatibility with the layer above it in the stack
- [var openMode: OpenConfiguration.Mode](diskimage/openmode.md)
  The open mode of the disk image, read-only or read-write.
- [var parentUUID: UUID?](diskimage/parentuuid.md)
  A UUID of the image that must be equal to the layer UUID of the layer beneath it in the stack.
- [var size: Int](diskimage/size.md)
  The logical size of the disk image in bytes.
- [let url: URL](diskimage/url.md)
  The URL of the disk image.
### Instance Methods
- [func appending(any DiskImage.CreationConfiguration & DiskImage.StackableLayer) throws -> any StackedImage](diskimage/appending(_:)-3pfqg.md)
  Appends a new layer to this disk image, creating or extending a stack
- [func appending(consuming DiskImage) throws -> any StackedImage](diskimage/appending(_:)-4wifj.md)
  Appends a layer to this disk image, creating or extending a stack.
- [func truncate(blockCount: Int) throws](diskimage/truncate(blockcount:).md)
  Truncate or extend the disk image to a new size.
### Enumerations
- [DiskImage.BlockSize](diskimage/blocksize-swift.enum.md)
  Values that represent the block size of a disk image.
- [DiskImage.Format](diskimage/format-swift.enum.md)
  Values that describe the disk image formats DiskImageKit supports.

## Relationships

### Inherited By
- [StackedImage](stackedimage.md)

## See Also

- [protocol StackedImage](stackedimage.md)
  The protocol for stacked disk images that contain multiple layers.
- [protocol OpenConfigurationProtocol](openconfigurationprotocol.md)
  The protocol for disk image open configurations.
- [struct OpenConfiguration](openconfiguration.md)
  A configuration to use for opening existing disk images.
- [OpenConfiguration.Mode](openconfiguration/mode-swift.enum.md)
  Open modes for disk images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage)*