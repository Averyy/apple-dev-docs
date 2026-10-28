# AVCaptionRenderer

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that renders captions for display at a particular time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
class AVCaptionRenderer
```

```objc
@interface AVCaptionRenderer : NSObject
```

## Overview

This object renders a caption scene for a given time from a collection of captions. If there aren’t any captions to display at the specified time, the renderer draws an empty flood fill with a zero alpha or a color.

## Topics

### Configuring the renderer
- [var captions: [AVCaption]](./avcaptionrenderer/captions.md)
  The captions to render.
- [var bounds: CGRect](./avcaptionrenderer/bounds.md)
  The drawing bounds of caption scenes.
### Determining scene changes
- [func captionSceneChanges(in: CMTimeRange) -> [AVCaptionRenderer.Scene]](./avcaptionrenderer/captionscenechanges%28in%29.md)
  Determine render time ranges within an enclosing time range to account for visual changes among captions.
- [AVCaptionRenderer.Scene](./avcaptionrenderer/scene.md)
  An object that holds a time range and an associated state which indicates when the renderer draws output.
### Rendering a caption
- [func render(in: CGContext, for: CMTime)](./avcaptionrenderer/render%28in,for%29.md)
  Draw the captions for the time you specify.
### Initializers
- [init()](./avcaptionrenderer/init%28%29.md)
### Type Methods
- [class func captionPreview(forProfileID: String, extendedLanguageTag: String?, renderSize: CGSize) -> NSAttributedString](./avcaptionrenderer/captionpreview%28forprofileid,extendedlanguagetag,rendersize%29.md)
  Generate a caption preview attributed string for the specified profile ID.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer)*