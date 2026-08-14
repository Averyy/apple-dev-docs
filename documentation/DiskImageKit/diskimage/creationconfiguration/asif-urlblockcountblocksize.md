# asif(url:blockCount:blockSize:)

**Framework**: DiskImageKit  
**Kind**: method

Returns an Apple sparse image format (ASIF) configuration for standalone or base images.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static func asif(url: URL, blockCount: Int, blockSize: DiskImage.BlockSize) -> Self
```

#### Return Value

An [`ASIFCreationConfiguration`](asifcreationconfiguration.md) instance for standalone use.

#### Discussion

Use this initializer when creating a standalone image, or a base image for a stack, using [`init(creating:)`](diskimage/init(creating:).md). To create a cache or overlay layer for a stacked disk image, use [`asifLayer(url:type:)`](diskimage/creationconfiguration/asiflayer(url:type:).md) instead.

The following example demonstrates how to create a ASIF disk image:

```None
_ = try DiskImage(creating: .asif(url: imageURL, blockCount: blockCount, blockSize: .bytes512))
```

## Parameters

- `url`: The [`URL`](https://developer.apple.com/documentation/foundation/url) for the disk image file.
- `blockCount`: Size of the disk image in blocks.
- `blockSize`: The [`DiskImage.BlockSize`](diskimage/blocksize-swift.enum.md) to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/creationconfiguration/asif(url:blockcount:blocksize:))*