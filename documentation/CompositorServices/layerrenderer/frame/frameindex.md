# frameIndex

**Framework**: Compositor Services  
**Kind**: property

The sequential index number of a frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var frameIndex: LayerFrameIndex { get }
```

#### Discussion

The layer assigns a unique index number to each frame, starting at the first frame and incrementing the index by `1` for each new frame.

## See Also

- [typealias LayerFrameIndex](layerframeindex.md)
  A frame index in the layer’s timeline.
- [typealias CompositorFrameIndex](compositorframeindex.md)
  The sequential index for a frame in the compositor’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/frameindex)*