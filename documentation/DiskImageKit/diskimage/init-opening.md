# init(opening:)

**Framework**: DiskImageKit  
**Kind**: init

Opens an existing disk image using the specified image URL.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
convenience init(opening configuration: some OpenConfigurationProtocol) throws
```

#### Discussion

Use this initializer to open any existing disk image — standalone or a disk image layer. To append this image to a stacked disk image, use [`appending(_:)`](diskimage/appending(_:)-4wifj.md). Encrypted disk images are not supported.

The following example demonstrates opening a disk image using a URL.

```None
let image = try DiskImage(opening: .open(url: imageURL))
```

> **Note**: [`CorruptedImageError`](corruptedimageerror.md) if the disk image contains invalid data. [`UnsupportedFormatError`](unsupportedformaterror.md) if the disk image format isn’t supported. `POSIXError` for file system errors such as file not found or permission denied.

## Parameters

- `configuration`: The configuration object that specifies the parameters for opening the disk image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/init(opening:))*