# init(aimeURL:device:)

**Framework**: Immersive Media Support  
**Kind**: init  
**Role**: Initializer

Creates a venue descriptor instance from an AIME file.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(aimeURL: URL, device: (any MTLDevice)? = nil) async throws
```

## Discussion

> **Throws**: This function throws exceptions if the input file doesn’t exist, or contains invalid information.

## Parameters

- `aimeURL`: A URL that points to a valid AIME file to load.
- `device`: The Metal device to use when loading calibration meshes into memory.

## See Also

### Creating a venue descriptor
- [init(device: (any MTLDevice)?)](./init%28device%29.md)
  Creates an empty venue descriptor instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/init(aimeurl:device:))*