# AVCaptionRenderer.Scene

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptionRendererScene : NSObject
```

## Overview

To render a scene, the object considers state like the existence of captions and regions, their temporal overlaps, and whether captions use animation effects. Your app can request time ranges where visual differences exist and use these time ranges to optimize drawing performance, like drawing once per scene. Alternatively, it can ignore scenes, and instead call [`render(in:for:)`](./render%28in,for%29.md) repeatedly, but this may have additional performance impact.

## Topics

### Inspecting the scene
- [var timeRange: CMTimeRange](./scene/timerange.md)
  The time range during which the system doesn’t modify the scene.
- [var hasActiveCaptions: Bool](./scene/hasactivecaptions.md)
  A Boolean value that indicates whether the scene contains one or more active captions.
- [var needsPeriodicRefresh: Bool](./scene/needsperiodicrefresh.md)
  A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining scene changes
- [func captionSceneChanges(in: CMTimeRange) -> [AVCaptionRenderer.Scene]](./captionscenechanges%28in%29.md)
  Determine render time ranges within an enclosing time range to account for visual changes among captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene)*