# init(aimeURL:device:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes a `VenueDescriptor` instance from an AIME file.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(aimeURL: URL, device: (any MTLDevice)? = nil) async throws
```

#### Discussion

> **Note**: This function will throw exceptions if the input file doesn’t exist, or contains invalid information.

## Parameters

- `aimeURL`: A URL pointing to a valid AIME file to load.
- `device`: The Metal Device to use when loading calibration meshes into memory.

## See Also

- [init(device: (any MTLDevice)?)](venuedescriptor/init(device:).md)
  Creates an empty `VenueDescriptor`, useful when creating a new `VenueDescriptor` in code (other than loading from an AIME file).


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/init(aimeurl:device:))*