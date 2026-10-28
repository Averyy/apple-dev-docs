# open(url:mode:)

**Framework**: DiskImageKit  
**Kind**: method  
**Role**: Type Method

Returns a configuration to use for opening a disk image.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static func open(url: URL, mode: OpenConfiguration.Mode = .automatic) -> Self
```

Available when `Self` is `OpenConfiguration`.

## Return Value

An [`OpenConfiguration`](../openconfiguration.md) instance.

## Discussion

The following example demonstrates how to open a disk image.

```
let image = try DiskImage(opening: .open(url: imageURL))
```

## Parameters

- `url`: A [`URL`](../../Foundation/url.md)  of the disk image file to open.
- `mode`: Mode in which to open the image (read-only or read-write).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/openconfigurationprotocol/open(url:mode:))*