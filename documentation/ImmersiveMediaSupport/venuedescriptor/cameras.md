# cameras

**Framework**: Immersive Media Support  
**Kind**: property  
**Role**: Instance Property

An array of all the immersive cameras contained in the venue descriptor (both original and dynamic).

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var cameras: [ImmersiveCamera] { get }
```

## See Also

### Configuring cameras
- [func addCamera(ImmersiveCamera) throws](./addcamera%28_%29.md)
  Adds a new immersive camera definition to the venue descriptor.
- [func removeCamera(id: String) throws](./removecamera%28id%29.md)
  Removes an immersive camera definition from the venue descriptor.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](./cameraviewmodel%28for%29.md)
  Returns the camera view model for the given immersive camera identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/cameras)*