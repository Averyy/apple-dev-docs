# removeCamera(id:)

**Framework**: Immersive Media Support  
**Kind**: method

Removes an immersive camera definition from the venue descriptor.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func removeCamera(id: String) throws
```

## Parameters

- `id`: The ID of the camera being removed.

## See Also

- [var cameras: [ImmersiveCamera]](venuedescriptor/cameras.md)
  An array of all the immersive cameras contained in the venue descriptor (both original and dynamic).
- [func addCamera(ImmersiveCamera) throws](venuedescriptor/addcamera(_:).md)
  Adds a new immersive camera definition to the venue descriptor.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](venuedescriptor/cameraviewmodel(for:).md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/removecamera(id:))*