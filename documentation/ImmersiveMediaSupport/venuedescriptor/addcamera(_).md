# addCamera(_:)

**Framework**: Immersive Media Support  
**Kind**: method  
**Role**: Instance Method

Adds a new immersive camera definition to the venue descriptor.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func addCamera(_ camera: ImmersiveCamera) throws
```

#### Discussion

> **Throws**: This function throws an error if the `ImmersiveCamera` information points to invalid data; for example, invalid calibration or mask files.

## Parameters

- `camera`: The [`ImmersiveCamera`](../immersivecamera.md) information to add.

## See Also

### Configuring cameras
- [var cameras: [ImmersiveCamera]](./cameras.md)
  An array of all the immersive cameras contained in the venue descriptor (both original and dynamic).
- [func removeCamera(id: String) throws](./removecamera%28id%29.md)
  Removes an immersive camera definition from the venue descriptor.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](./cameraviewmodel%28for%29.md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/addcamera(_:))*