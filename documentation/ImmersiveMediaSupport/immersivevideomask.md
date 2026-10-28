# ImmersiveVideoMask

**Framework**: Immersive Media Support  
**Kind**: struct  
**Role**: Structure

A video mask to use during video rendering to smooth the edges of the mesh.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ImmersiveVideoMask
```

## Overview

This type holds the generated video mask texture and its relevant information.

## Topics

### Instance Properties
- [var layout: ImmersiveVideoMask.Layout](./immersivevideomask/layout-swift.property.md)
  The layout of this mask, see [`ImmersiveVideoMask.Layout`](./immersivevideomask/layout-swift.enum.md) for more details.
- [var texture: any MTLTexture](./immersivevideomask/texture.md)
  The mask texture ready for rendering.
- [var isInEquirectangularProjection: Bool](./immersivevideomask/isinequirectangularprojection.md)
  A Boolean value that indicates whether the generated mask texture is in equirectangular projection space. If `true`, the app renderer needs to transform vertices of the mesh to equirectangular projection space to generate UVs to access the mask texture.
### Enumerations
- [ImmersiveVideoMask.Layout](./immersivevideomask/layout-swift.enum.md)
  A value that represents the layout of the video mask.
### Operators
- [static func == (ImmersiveVideoMask, ImmersiveVideoMask) -> Bool](./immersivevideomask/eqeq%28_,_%29.md)
  Compares two masks.
### Initializers
- [init(layout: ImmersiveVideoMask.Layout, isInEquirectangularProjection: Bool, texture: any MTLTexture)](./immersivevideomask/init%28layout,isinequirectangularprojection,texture%29.md)
  Creates an immersive video mask object.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Immersive video rendering support
- [struct ImmersiveVideoFrame](./immersivevideoframe.md)
  A type that represents an immersive video frame, including its layout, presentation time, and pixel buffer data.
- [struct ImmersiveCameraViewModel](./immersivecameraviewmodel.md)
  A view model that holds all the resources needed to render an immersive camera view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask)*