# raw(url:blockCount:)

**Framework**: DiskImageKit  
**Kind**: method  
**Role**: Type Method

Returns a RAW configuration for standalone or base images.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static func raw(url: URL, blockCount: Int) -> Self
```

Available when `Self` is `RAWCreationConfiguration`.

#### Return Value

A [`RAWCreationConfiguration`](../../rawcreationconfiguration.md) instance.

#### Discussion

The framework only supports the 512-byte block size for RAW images.

The following example demonstrates how to create a RAW disk image.

```
_ = try DiskImage(creating: .raw(url: imageURL, blockCount: blockCount))
```

## Parameters

- `url`: The [`URL`](../../../Foundation/url.md) for the disk image file.
- `blockCount`: Size of the disk image in blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/creationconfiguration/raw(url:blockcount:))*