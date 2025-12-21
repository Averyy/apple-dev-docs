# LayerRenderer.RenderQuality

**Framework**: Compositor Services  
**Kind**: struct

Render quality controls the quality which drawing happens at.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct RenderQuality
```

#### Overview

This can be used to increase the quality of what users see, however this directly impacts the memory allocated for resources which is billed to the app as well as per-frame GPU time. The app should monitor its frame rate to ensure its not regularly missing frames and will likely need to change the quality based on scene complexity that is being shown.

To control the memory allocated for resources

To control the per-frame GPU cost

## Topics

### Initializers
- [init(Float)](layerrenderer/renderquality-swift.struct/init(_:).md)
- [init(rawValue: Float)](layerrenderer/renderquality-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/renderquality-swift.struct)*