# cameras

**Framework**: Immersive Media Support  
**Kind**: property

Property contains information about all the ImmersiveCameras contained in this VenueDescriptor.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final var cameras: [ImmersiveCamera] { get }
```

## See Also

- [func addCamera(ImmersiveCamera) throws](venuedescriptor/addcamera(_:).md)
  Adds a new ImmersiveCamera definition to this VenueDescriptor.
- [func removeCamera(id: String) throws](venuedescriptor/removecamera(id:).md)
  Removes an ImmersiveCamera definition from this VenueDescriptor.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](venuedescriptor/cameraviewmodel(for:).md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/cameras)*