# init(aimeData:device:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a venue descriptor instance from memory.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(aimeData: Data, device: (any MTLDevice)? = nil) async throws
```

## Parameters

- `aimeData`: The Data that contains the venue descriptor to parse.
- `device`: The Metal device to use when loading calibration meshes into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/init(aimedata:device:))*