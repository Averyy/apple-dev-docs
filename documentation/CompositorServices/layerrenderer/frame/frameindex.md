# frameIndex

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The sequential index number of a frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var frameIndex: LayerFrameIndex { get }
```

```c
cp_layer_frame_index_t cp_frame_get_frame_index(cp_frame_t frame);
```

## Discussion

The layer assigns a unique index number to each frame, starting at the first frame and incrementing the index by `1` for each new frame.

## See Also

### Getting frame-related details
- [typealias LayerFrameIndex](../../layerframeindex.md)
  A frame index in the layer’s timeline.
- [typealias CompositorFrameIndex](../../compositorframeindex.md)
  The sequential index for a frame in the compositor’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/frameindex)*