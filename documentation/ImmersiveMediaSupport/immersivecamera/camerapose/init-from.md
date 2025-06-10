# init(from:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [init(position: simd_float3, rotation: simd_float3)](immersivecamera/camerapose/init(position:rotation:).md)
  Initializes using the given camera position and camera rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecamera/camerapose/init(from:))*