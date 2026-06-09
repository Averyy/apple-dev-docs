# open(url:mode:)

**Framework**: DiskImageKit  
**Kind**: method

Returns a configuration to use for opening a disk image.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static func open(url: URL, mode: OpenConfiguration.Mode = .automatic) -> Self
```

#### Return Value

An [`OpenConfiguration`](openconfiguration.md) instance.

#### Discussion

The following example demonstrates how to open a disk image.

```None
let image = try DiskImage(opening: .open(url: imageURL))
```

## Parameters

- `url`: A [`URL`](https://developer.apple.com/documentation/Foundation/URL)  of the disk image file to open.
- `mode`: Mode in which to open the image (read-only or read-write).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/openconfigurationprotocol/open(url:mode:))*