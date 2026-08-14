# ImmersivePreviewRenderer

**Framework**: Immersive Media Support  
**Kind**: class

An object that renders an immersive video frame into a texture and exposes the command buffer for presentation.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
class ImmersivePreviewRenderer
```

#### Overview

`ImmersivePreviewRenderer` provides a high-level interface for rendering immersive video content with support for stereoscopic rendering, presentation commands, and venue-specific camera models. It manages the rendering pipeline including geometry setup, texture management, and frame processing.

The renderer supports two rendering modes:

- **macOS**: Rendering directly to a specified texture with manual camera control via rotation and field of view parameters.
- **visionOS**: Rendering to `LayerRenderer.Drawable` instances with automatic head tracking and view management.

Create a renderer with a venue descriptor that defines the camera models and rendering geometry:

```swift
let venueDescriptor = try VenueDescriptor(aimeFileURL: aimeURL)
let renderer = ImmersivePreviewRenderer(venueDescriptor: venueDescriptor)
```

On macOS, render frames directly to a texture:

```swift
await renderer.process(
    frame,
    for: .left,
    rotation: currentRotation,
    fieldOfView: 90,
    presentationDescriptor: descriptor,
    renderTexture: drawable.texture
)
```

On visionOS, integrate with CompositorServices for immersive rendering:

```swift
await renderer.process(
    frame,
    presentationDescriptor: descriptor,
    drawable: drawable
)
```

Finally, present and commit command buffer:

```swift
if let commandBuffer = renderer.commandBuffer {
    commandBuffer.present(drawable)
    commandBuffer.commit()
}
```

## Topics

### Initializers
- [init(device: (any MTLDevice)?, venueDescriptor: VenueDescriptor?, depthPixelFormat: MTLPixelFormat?, colorPixelFormat: MTLPixelFormat?)](immersivepreviewrenderer/init(device:venuedescriptor:depthpixelformat:colorpixelformat:).md)
  Creates an immersive preview renderer.
### Instance Properties
- [var commandBuffer: (any MTLCommandBuffer)?](immersivepreviewrenderer/commandbuffer.md)
  The command buffer of the render.
- [var venueDescriptor: VenueDescriptor?](immersivepreviewrenderer/venuedescriptor.md)
  The venue descriptor for rendering immersive video frames.
### Instance Methods
- [func process(ImmersiveVideoFrame, for: ImmersivePreviewRenderer.Eye, rotation: Rotation3D, fieldOfView: Float, presentationDescriptor: PresentationDescriptor, renderTexture: any MTLTexture) async](immersivepreviewrenderer/process(_:for:rotation:fieldofview:presentationdescriptor:rendertexture:).md)
  Performs the rendering of an immersive video frame.
- [func process(ImmersiveVideoFrame, presentationDescriptor: PresentationDescriptor, drawable: LayerRenderer.Drawable) async](immersivepreviewrenderer/process(_:presentationdescriptor:drawable:).md)
  Performs the rendering of an immersive video frame.
### Enumerations
- [ImmersivePreviewRenderer.Eye](immersivepreviewrenderer/eye.md)
  An enumeration that represents the eye of the user.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class ImmersiveMediaPreviewMessagingProtocol](immersivemediapreviewmessagingprotocol.md)
  An object that represents the messaging protocol a remote preview sender and receiver use to communicate.
- [class ImmersiveMediaRemotePreviewSender](immersivemediaremotepreviewsender.md)
  An observable object that helps an app send the required data to all connected receiver applications to help facilitate the complete preview of the immersive media playback.
- [class ImmersiveMediaRemotePreviewReceiver](immersivemediaremotepreviewreceiver.md)
  An observable object that helps applications handle receiving commands and data sent from an immersive media remote preview sender object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivepreviewrenderer)*