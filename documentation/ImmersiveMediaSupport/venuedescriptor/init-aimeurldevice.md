# init(aimeURL:device:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a venue descriptor instance from an AIME file.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(aimeURL: URL, device: (any MTLDevice)? = nil) async throws
```

#### Discussion

> **Note**: This function throws exceptions if the input file doesn’t exist, or contains invalid information.

## Parameters

- `aimeURL`: A URL that points to a valid AIME file to load.
- `device`: The Metal device to use when loading calibration meshes into memory.

## See Also

- [init(device: (any MTLDevice)?)](venuedescriptor/init(device:).md)
  Creates an empty venue descriptor instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/init(aimeurl:device:))*