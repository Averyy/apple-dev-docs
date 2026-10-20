# presentationFrameIndex

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The sequential index of a drawable’s frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var presentationFrameIndex: CompositorFrameIndex { get }
```

```c
cp_compositor_frame_index_t cp_drawable_get_presentation_frame_index(cp_drawable_t drawable);
```

#### Discussion

When your immersive space becomes visible, you start drawing frames of content. Compositor Services assigns a sequential index to each frame to indicate its position in the final output. You can use these indexes to differentiate frames during drawing or predict future frame indexes. For example, you might start playback of an audio file when a specific frame appears.

## See Also

### Synchronizing the drawing operation
- [var frameTiming: LayerRenderer.Frame.Timing](./frametiming.md)
  The timing information for the drawable’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/presentationframeindex)*