# CameraFrame.Sample.Parameters

**Framework**: ARKit  
**Kind**: struct

A frame’s parameters, such as the camera type, intrinsics, timestamps, exposure, and so on.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Parameters
```

## Topics

### Getting frame parameters
- [var cameraPosition: CameraFrameProvider.CameraPosition](cameraframe/sample/parameters-swift.struct/cameraposition.md)
  The camera position.
- [var cameraType: CameraFrameProvider.CameraType](cameraframe/sample/parameters-swift.struct/cameratype.md)
- [var captureTimestamp: TimeInterval](cameraframe/sample/parameters-swift.struct/capturetimestamp.md)
  The capture timestamp.
- [var colorTemperature: Int](cameraframe/sample/parameters-swift.struct/colortemperature.md)
  The white balance correlated color temperature in kelvin.
- [var exposureDuration: CFTimeInterval](cameraframe/sample/parameters-swift.struct/exposureduration.md)
  The camera frame exposure duration in seconds.
- [var extrinsics: simd_float4x4](cameraframe/sample/parameters-swift.struct/extrinsics.md)
  The camera extrinsics.
- [var intrinsics: simd_float3x3](cameraframe/sample/parameters-swift.struct/intrinsics.md)
- [var midExposureTimestamp: TimeInterval](cameraframe/sample/parameters-swift.struct/midexposuretimestamp.md)
  The mid exposure timestamp.
### Instance Properties
- [var description: String](cameraframe/sample/parameters-swift.struct/description.md)
  A textual representation of these camera frame parameters.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var parameters: CameraFrame.Sample.Parameters](cameraframe/sample/parameters-swift.property.md)
  The frame’s parameters.
- [var pixelBuffer: CVPixelBuffer](cameraframe/sample/pixelbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/sample/parameters-swift.struct)*