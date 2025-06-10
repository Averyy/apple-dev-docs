# ImmersiveVideoMask

**Framework**: Immersive Media Support  
**Kind**: struct

A video mask to use during video rendering to smooth the edges of the mesh.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveVideoMask
```

#### Overview

This type holds the generated video mask texture and its relevant information.

## Topics

### Initializers
- [init(layout: ImmersiveVideoMask.Layout, isDynamic: Bool, texture: any MTLTexture)](immersivevideomask/init(layout:isdynamic:texture:).md)
  Creates an ImmersiveVideoMask.
### Instance Properties
- [var isDynamic: Bool](immersivevideomask/isdynamic.md)
  Flag to indicate if this mask was generated from a [`ImmersiveDynamicMask`](immersivedynamicmask.md).
- [var layout: ImmersiveVideoMask.Layout](immersivevideomask/layout-swift.property.md)
  The layout of this mask, see [`ImmersiveVideoMask.Layout`](immersivevideomask/layout-swift.enum.md) for more details.
- [var texture: any MTLTexture](immersivevideomask/texture.md)
  The mask texture ready to be used for rendering.
### Enumerations
- [ImmersiveVideoMask.Layout](immersivevideomask/layout-swift.enum.md)
  Represents the layout of the video mask
### Operators
- [static func == (ImmersiveVideoMask, ImmersiveVideoMask) -> Bool](immersivevideomask/==(_:_:).md)
  Compares two masks.
### Default Implementations
- [Equatable Implementations](immersivevideomask/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ImmersiveCameraViewModel](immersivecameraviewmodel.md)
  A view model that holds all the resources needed to render an immersive camera view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask)*