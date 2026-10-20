# CameraFrame.Sample.Parameters

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

A frame’s parameters, such as the camera type, intrinsics, timestamps, exposure, and so on.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Parameters
```

## Topics

### Getting frame parameters
- [var cameraPosition: CameraFrameProvider.CameraPosition](./parameters-swift.struct/cameraposition.md)
  The camera position.
- [var cameraType: CameraFrameProvider.CameraType](./parameters-swift.struct/cameratype.md)
- [var captureTimestamp: TimeInterval](./parameters-swift.struct/capturetimestamp.md)
  The capture timestamp.
- [var colorTemperature: Int](./parameters-swift.struct/colortemperature.md)
  The white balance correlated color temperature in kelvin.
- [var exposureDuration: TimeInterval](./parameters-swift.struct/exposureduration.md)
  The camera frame exposure duration in seconds.
- [var extrinsics: simd_float4x4](./parameters-swift.struct/extrinsics.md)
  The camera extrinsics.
- [var intrinsics: simd_float3x3](./parameters-swift.struct/intrinsics.md)
- [var midExposureTimestamp: TimeInterval](./parameters-swift.struct/midexposuretimestamp.md)
  The mid exposure timestamp.
### Operators
- [static func == (CameraFrame.Sample.Parameters, CameraFrame.Sample.Parameters) -> Bool](./parameters-swift.struct/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two camera frame parameters are equal.
### Instance Properties
- [var description: String](./parameters-swift.struct/description.md)
  A textual representation of these camera frame parameters.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting camera frame samples
- [var parameters: CameraFrame.Sample.Parameters](./parameters-swift.property.md)
  The frame’s parameters.
- [var pixelBuffer: CVPixelBuffer](./pixelbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/sample/parameters-swift.struct)*