# sample(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the camera frame sample for a given camera position.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func sample(for position: CameraFrameProvider.CameraPosition) -> CameraFrame.Sample?
```

## Return Value

The camera frame sample, or `nil` if no sample is available for the given camera position.

## Parameters

- `position`: The camera position to get the sample for.

## See Also

### Getting camera frame information
- [var primarySample: CameraFrame.Sample](./primarysample.md)
  Gets the primary frame sample for a camera frame.
- [CameraFrame.Sample](./sample.md)
  Information that describes a sample from a camera frame.
- [var description: String](./description.md)
  A textual representation of this camera frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframe/sample(for:))*