# cameras

**Framework**: Immersive Media Support  
**Kind**: property

An array of all the immersive cameras contained in the venue descriptor.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var cameras: [ImmersiveCamera] { get }
```

## See Also

- [func addCamera(ImmersiveCamera) throws](venuedescriptor/addcamera(_:).md)
  Adds a new immersive camera definition to the venue descriptor.
- [func removeCamera(id: String) throws](venuedescriptor/removecamera(id:).md)
  Removes an immersive camera definition from the venue descriptor.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](venuedescriptor/cameraviewmodel(for:).md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/cameras)*