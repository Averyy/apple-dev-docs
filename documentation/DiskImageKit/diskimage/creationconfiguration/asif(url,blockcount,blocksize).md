# asif(url:blockCount:blockSize:)

**Framework**: DiskImageKit  
**Kind**: method  
**Role**: Type Method

Returns an Apple sparse image format (ASIF) configuration for standalone or base images.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static func asif(url: URL, blockCount: Int, blockSize: DiskImage.BlockSize) -> Self
```

Available when `Self` is `ASIFCreationConfiguration`.

#### Return Value

An [`ASIFCreationConfiguration`](../../asifcreationconfiguration.md) instance for standalone use.

#### Discussion

Use this initializer when creating a standalone image, or a base image for a stack, using [`init(creating:)`](../init%28creating%29.md). To create a cache or overlay layer for a stacked disk image, use [`asifLayer(url:type:)`](./asiflayer%28url,type%29.md) instead.

The following example demonstrates how to create a ASIF disk image:

```
_ = try DiskImage(creating: .asif(url: imageURL, blockCount: blockCount, blockSize: .bytes512))
```

## Parameters

- `url`: The [`URL`](../../../Foundation/url.md) for the disk image file.
- `blockCount`: Size of the disk image in blocks.
- `blockSize`: The [`DiskImage.BlockSize`](../blocksize-swift.enum.md) to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/creationconfiguration/asif(url:blockcount:blocksize:))*