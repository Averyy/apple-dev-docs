# init(url:mode:)

**Framework**: DiskImageKit  
**Kind**: init

Creates a configuration for opening a disk image.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init(url: URL, mode: OpenConfiguration.Mode = .automatic)
```

## Parameters

- `url`: The [`URL`](https://developer.apple.com/documentation/Foundation/URL) of the disk image file to open.
- `mode`: The mode in which to open the image (read-only or read-write).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/openconfiguration/init(url:mode:))*