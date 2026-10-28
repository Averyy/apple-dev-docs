# cameraViewModel(for:)

**Framework**: Immersive Media Support  
**Kind**: method  
**Role**: Instance Method

Returns the camera view model for the given immersive camera identifier.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func cameraViewModel(for id: String) -> ImmersiveCameraViewModel?
```

## Return Value

ImmersiveCameraViewModel describing the geometries, mask and other information to be used for that camera for rendering.

## Parameters

- `id`: Identifier string of the immersive camera

## See Also

### Configuring cameras
- [var cameras: [ImmersiveCamera]](./cameras.md)
  An array of all the immersive cameras contained in the venue descriptor (both original and dynamic).
- [func addCamera(ImmersiveCamera) throws](./addcamera%28_%29.md)
  Adds a new immersive camera definition to the venue descriptor.
- [func removeCamera(id: String) throws](./removecamera%28id%29.md)
  Removes an immersive camera definition from the venue descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/cameraviewmodel(for:))*