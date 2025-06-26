# init(aimeData:device:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes an `VenueDescriptor` instance from memory.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(aimeData: Data, device: (any MTLDevice)? = nil) async throws
```

## Parameters

- `aimeData`: Data containing the venue descriptor to be parsed.
- `device`: The Metal Device to use when loading calibration meshes into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/init(aimedata:device:))*