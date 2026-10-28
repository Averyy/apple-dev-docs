# LayerRenderer.RenderQuality

**Framework**: Compositor Services  
**Kind**: struct  
**Role**: Structure

Render quality controls the quality which drawing happens at.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct RenderQuality
```

```c
typedef float cp_render_quality_t;
```

## Overview

This can be used to increase the quality of what users see, however this directly impacts the memory allocated for resources which is billed to the app as well as per-frame GPU time. The app should monitor its frame rate to ensure its not regularly missing frames and will likely need to change the quality based on scene complexity that is being shown.

To control the memory allocated for resources

To control the per-frame GPU cost

## Topics

### Initializers
- [init(Float)](./renderquality-swift.struct/init%28_%29.md)
- [init(rawValue: Float)](./renderquality-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/renderquality-swift.struct)*