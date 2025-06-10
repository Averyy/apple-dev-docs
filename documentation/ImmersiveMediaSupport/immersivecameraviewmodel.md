# ImmersiveCameraViewModel

**Framework**: Immersive Media Support  
**Kind**: struct

A view model that holds all the resources needed to render an immersive camera view.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveCameraViewModel
```

#### Overview

App needs to query this type instance from [`VenueDescriptor`](venuedescriptor.md) instance given the immersive camera identifier.

## Topics

### Instance Properties
- [var cameraID: String](immersivecameraviewmodel/cameraid.md)
  The camera identifier string of the Immersive camera associated with this view model.
- [var environmentBackdrop: MDLAsset?](immersivecameraviewmodel/environmentbackdrop.md)
  The environment backdrop associated with the immersive camera view
- [var leftEye: MDLMesh](immersivecameraviewmodel/lefteye.md)
  Left eye mesh associated with the Immersive camera view.
- [var mask: ImmersiveVideoMask?](immersivecameraviewmodel/mask.md)
  Generated immersive video mask associated with the immersive camera view
- [var rightEye: MDLMesh](immersivecameraviewmodel/righteye.md)
  Right eye mesh associated with the Immersive camera view.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ImmersiveVideoMask](immersivevideomask.md)
  A video mask to use during video rendering to smooth the edges of the mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameraviewmodel)*