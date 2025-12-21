# cameraViewModel(for:)

**Framework**: Immersive Media Support  
**Kind**: method

Returns the camera view model for the given immersive camera identifier.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

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
  An array of all the immersive cameras contained in the venue descriptor.
- [func addCamera(ImmersiveCamera) throws](venuedescriptor/addcamera(_:).md)
  Adds a new immersive camera definition to the venue descriptor.
- [func removeCamera(id: String) throws](venuedescriptor/removecamera(id:).md)
  Removes an immersive camera definition from the venue descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/cameraviewmodel(for:))*