# CompositorFrameIndex

**Framework**: Compositor Services  
**Kind**: typealias

The sequential index for a frame in the compositor’s timeline.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
typealias CompositorFrameIndex = UInt64
```

#### Discussion

During the creation of your content, the compositor creates frames for you to render your content. This type stores the index the compositor assigns to that frame. The compositor presents frames sequentially based on their indexes.

## See Also

- [var frameIndex: LayerFrameIndex](layerrenderer/frame/frameindex.md)
  The sequential index number of a frame.
- [typealias LayerFrameIndex](layerframeindex.md)
  A frame index in the layer’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/compositorframeindex)*