# init(data:device:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes an VenueDescriptor instance from memory.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(data: Data, device: (any MTLDevice)? = nil) async throws
```

## Parameters

- `data`: Data containing the venue descriptor to be parsed.
- `device`: The Metal Device to use when loading calibration meshes into memory.

## See Also

- [init(device: (any MTLDevice)?)](venuedescriptor/init(device:).md)
  Creates an empty VenueDescriptor, useful when creating a new VenueDescriptor in code (other than loading from an AIME file).
- [convenience init(aimeURL: URL, device: (any MTLDevice)?) async throws](venuedescriptor/init(aimeurl:device:).md)
  Initializes an VenueDescriptor instance from an AIME file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/init(data:device:))*