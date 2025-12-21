# AVCaptionRenderer.Scene

**Framework**: AVFoundation  
**Kind**: class

An object that holds a time range and an associated state which indicates when the renderer draws output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class Scene
```

#### Overview

To render a scene, the object considers state like the existence of captions and regions, their temporal overlaps, and whether captions use animation effects. Your app can request time ranges where visual differences exist and use these time ranges to optimize drawing performance, like drawing once per scene. Alternatively, it can ignore scenes, and instead call [`render(in:for:)`](avcaptionrenderer/render(in:for:).md) repeatedly, but this may have additional performance impact.

## Topics

### Inspecting the scene
- [var timeRange: CMTimeRange](avcaptionrenderer/scene/timerange.md)
  The time range during which the system doesn’t modify the scene.
- [var hasActiveCaptions: Bool](avcaptionrenderer/scene/hasactivecaptions.md)
  A Boolean value that indicates whether the scene contains one or more active captions.
- [var needsPeriodicRefresh: Bool](avcaptionrenderer/scene/needsperiodicrefresh.md)
  A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func captionSceneChanges(in: CMTimeRange) -> [AVCaptionRenderer.Scene]](avcaptionrenderer/captionscenechanges(in:).md)
  Determine render time ranges within an enclosing time range to account for visual changes among captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene)*