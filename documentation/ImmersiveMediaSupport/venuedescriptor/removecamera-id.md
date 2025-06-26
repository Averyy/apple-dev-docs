# removeCamera(id:)

**Framework**: Immersive Media Support  
**Kind**: method

Removes an `ImmersiveCamera` definition from this `VenueDescriptor`.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func removeCamera(id: String) throws
```

## Parameters

- `id`: The ID of the camera being removed.

## See Also

- [var cameras: [ImmersiveCamera]](venuedescriptor/cameras.md)
  Property contains information about all the ImmersiveCameras contained in this `VenueDescriptor`.
- [func addCamera(ImmersiveCamera) throws](venuedescriptor/addcamera(_:).md)
  Adds a new `ImmersiveCamera` definition to this `VenueDescriptor`.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](venuedescriptor/cameraviewmodel(for:).md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/removecamera(id:))*