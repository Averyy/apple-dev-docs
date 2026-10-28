# CameraFrame.Sample

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Information that describes a sample from a camera frame.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Sample
```

## Overview

Use this structure to access information about a sample from a [`CameraFrame`](../cameraframe.md), such as the frame’s settings and parameters, a pixel buffer that contains the sample’s data, and so on.

## Topics

### Inspecting camera frame samples
- [var parameters: CameraFrame.Sample.Parameters](./sample/parameters-swift.property.md)
  The frame’s parameters.
- [CameraFrame.Sample.Parameters](./sample/parameters-swift.struct.md)
  A frame’s parameters, such as the camera type, intrinsics, timestamps, exposure, and so on.
- [var pixelBuffer: CVPixelBuffer](./sample/pixelbuffer.md)
### Operators
- [static func == (CameraFrame.Sample, CameraFrame.Sample) -> Bool](./sample/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two camera frame samples are equal.
### Instance Properties
- [var buffer: CVReadOnlyPixelBuffer](./sample/buffer.md)
  The pixel buffer.
- [var description: String](./sample/description.md)
  A textual representation of this camera frame sample.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting camera frame information
- [var primarySample: CameraFrame.Sample](./primarysample.md)
  Gets the primary frame sample for a camera frame.
- [func sample(for: CameraFrameProvider.CameraPosition) -> CameraFrame.Sample?](./sample%28for%29.md)
  Returns the camera frame sample for a given camera position.
- [var description: String](./description.md)
  A textual representation of this camera frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/sample)*