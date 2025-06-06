# sample(for:)

**Framework**: ARKit  
**Kind**: method

Returns the camera frame sample for a given camera position.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func sample(for position: CameraFrameProvider.CameraPosition) -> CameraFrame.Sample?
```

#### Return Value

The camera frame sample, or `nil` if no sample is available for the given camera position.

## Parameters

- `position`: The camera position to get the sample for.

## See Also

- [var primarySample: CameraFrame.Sample](cameraframe/primarysample.md)
  Gets the primary frame sample for a camera frame.
- [CameraFrame.Sample](cameraframe/sample.md)
  Information that describes a sample from a camera frame.
- [var description: String](cameraframe/description.md)
  A textual representation of this camera frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/sample(for:))*