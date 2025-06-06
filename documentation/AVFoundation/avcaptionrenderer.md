# AVCaptionRenderer

**Framework**: AVFoundation  
**Kind**: class

An object that renders captions for display at a particular time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionRenderer
```

#### Overview

This object renders a caption scene for a given time from a collection of captions. If there aren’t any captions to display at the specified time, the renderer draws an empty flood fill with a zero alpha or a color.

## Topics

### Configuring the Renderer
- [var captions: [AVCaption]](avcaptionrenderer/captions.md)
  The captions to render.
- [var bounds: CGRect](avcaptionrenderer/bounds.md)
  The drawing bounds of caption scenes.
### Determining Scene Changes
- [func captionSceneChanges(in: CMTimeRange) -> [AVCaptionRenderer.Scene]](avcaptionrenderer/captionscenechanges(in:).md)
  Determine render time ranges within an enclosing time range to account for visual changes among captions.
- [AVCaptionRenderer.Scene](avcaptionrenderer/scene.md)
  An object that holds a time range and an associated state which indicates when the renderer draws output.
### Rendering a Caption
- [func render(in: CGContext, for: CMTime)](avcaptionrenderer/render(in:for:).md)
  Draw the captions for the time you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer)*