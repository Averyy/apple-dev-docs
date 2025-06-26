# cameraViewModel(for:)

**Framework**: Immersive Media Support  
**Kind**: method

Returns the camera view model for the given immersive camera identifier.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func cameraViewModel(for id: String) -> ImmersiveCameraViewModel?
```

#### Return Value

ImmersiveCameraViewModel describing the geometries, mask and other information to be used for that camera for rendering.

## Parameters

- `id`: Identifier string of the immersive camera

## See Also

- [var cameras: [ImmersiveCamera]](venuedescriptor/cameras.md)
  Property contains information about all the ImmersiveCameras contained in this `VenueDescriptor`.
- [func addCamera(ImmersiveCamera) throws](venuedescriptor/addcamera(_:).md)
  Adds a new `ImmersiveCamera` definition to this `VenueDescriptor`.
- [func removeCamera(id: String) throws](venuedescriptor/removecamera(id:).md)
  Removes an `ImmersiveCamera` definition from this `VenueDescriptor`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/cameraviewmodel(for:))*