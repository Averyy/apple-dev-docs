# addCamera(_:)

**Framework**: Immersive Media Support  
**Kind**: method

Adds a new immersive camera definition to the venue descriptor.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func addCamera(_ camera: ImmersiveCamera) throws
```

#### Discussion

> **Note**: This function throws an error if the `ImmersiveCamera` information points to invalid data; for example, invalid calibration or mask files.

## Parameters

- `camera`: The   information to add.

## See Also

- [var cameras: [ImmersiveCamera]](venuedescriptor/cameras.md)
  An array of all the immersive cameras contained in the venue descriptor.
- [func removeCamera(id: String) throws](venuedescriptor/removecamera(id:).md)
  Removes an immersive camera definition from the venue descriptor.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](venuedescriptor/cameraviewmodel(for:).md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/addcamera(_:))*