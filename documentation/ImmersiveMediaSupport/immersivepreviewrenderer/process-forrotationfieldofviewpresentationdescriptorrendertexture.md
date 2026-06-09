# process(_:for:rotation:fieldOfView:presentationDescriptor:renderTexture:)

**Framework**: Immersive Media Support  
**Kind**: method

Performs the rendering of an immersive video frame.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func process(_ frame: ImmersiveVideoFrame, for eye: ImmersivePreviewRenderer.Eye = .left, rotation: Rotation3D = .identity, fieldOfView: Float = 90, presentationDescriptor: PresentationDescriptor, renderTexture: any MTLTexture) async
```

#### Discussion

This method is available on macOS and provides manual control over camera pose and projection parameters. It updates the camera pose based on the provided rotation, configures the projection matrix using the specified field of view, and processes presentation commands to determine the active camera and rendering parameters.

The rendering operation is asynchronous and completes when the frame has been submitted to the GPU. Access [`commandBuffer`](immersivepreviewrenderer/commandbuffer.md) after this method returns to retrieve the command buffer for synchronization.

## Parameters

- `frame`: The `ImmersiveVideoFrame` to render.
- `eye`: The eye of the user.
- `rotation`: The rotation to apply to the `ImmersiveVideoFrame`.
- `fieldOfView`: The field of view to be used when processing frame.
- `presentationDescriptor`: The presentation descriptor for the commands to process on the frame.
- `renderTexture`: The texture to render to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivepreviewrenderer/process(_:for:rotation:fieldofview:presentationdescriptor:rendertexture:))*