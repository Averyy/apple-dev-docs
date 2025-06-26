# addCamera(_:)

**Framework**: Immersive Media Support  
**Kind**: method

Adds a new `ImmersiveCamera` definition to this `VenueDescriptor`.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func addCamera(_ camera: ImmersiveCamera) throws
```

#### Discussion

> **Note**: This function will throw an error if the `ImmersiveCamera` information points to invalid data, for example invalid calibration or mask files.

## Parameters

- `camera`: The   information to add.

## See Also

- [var cameras: [ImmersiveCamera]](venuedescriptor/cameras.md)
  Property contains information about all the ImmersiveCameras contained in this `VenueDescriptor`.
- [func removeCamera(id: String) throws](venuedescriptor/removecamera(id:).md)
  Removes an `ImmersiveCamera` definition from this `VenueDescriptor`.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](venuedescriptor/cameraviewmodel(for:).md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/addcamera(_:))*