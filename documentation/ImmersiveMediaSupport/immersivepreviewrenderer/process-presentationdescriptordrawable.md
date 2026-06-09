# process(_:presentationDescriptor:drawable:)

**Framework**: Immersive Media Support  
**Kind**: method

Performs the rendering of an immersive video frame.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func process(_ frame: ImmersiveVideoFrame, presentationDescriptor: PresentationDescriptor, drawable: LayerRenderer.Drawable) async
```

#### Discussion

This method is available on visionOS and integrates with the CompositorServices framework to provide head-tracked stereoscopic rendering. It automatically processes both left and right eye views, applies device anchor transforms for head tracking.

The rendering operation is asynchronous and completes when the frame has been submitted to the GPU. Access [`commandBuffer`](immersivepreviewrenderer/commandbuffer.md) after this method returns to retrieve the command buffer for synchronization.

## Parameters

- `frame`: The `ImmersiveVideoFrame` to render.
- `presentationDescriptor`: The presentation descriptor for the commands to process on the frame.
- `drawable`: The drawable to render to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivepreviewrenderer/process(_:presentationdescriptor:drawable:))*