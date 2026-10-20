# AVVideoCompositionCoreAnimationTool

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object used to incorporate Core Animation into a video composition.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVVideoCompositionCoreAnimationTool
```

```objc
@interface AVVideoCompositionCoreAnimationTool : NSObject
```

#### Overview

Any animations will be interpreted on the video’s timeline, not real-time, so you should:

1. Set animations’ [`beginTime`](../QuartzCore/camediatiming/begintime.md) property to [`AVCoreAnimationBeginTimeAtZero`](./avcoreanimationbegintimeatzero.md) rather than `0` (which CoreAnimation replaces with [`CACurrentMediaTime()`](../QuartzCore/cacurrentmediatime%28%29.md));
2. Set [`isRemovedOnCompletion`](../QuartzCore/caanimation/isremovedoncompletion.md) to [`false`](../Swift/false.md) on animations so they are not automatically removed;
3. Avoid using layers that are associated with [`UIView`](../UIKit/uiview.md) objects.

## Topics

### Creating a composition tool
- [convenience init(additionalLayer: sending CALayer, asTrackID: CMPersistentTrackID)](./avvideocompositioncoreanimationtool/init%28additionallayer,astrackid%29.md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayer: CALayer, in: CALayer)](./avvideocompositioncoreanimationtool/init%28postprocessingasvideolayer,in%29.md)
  Composes the composited video frame with a Core Animation layer.
- [convenience init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](./avvideocompositioncoreanimationtool/init%28postprocessingasvideolayers,in%29.md)
  Composes the composited video frames with the Core Animation layer.
- [convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)](./avvideocompositioncoreanimationtool/init%28configuration%29.md)
  Compose the composited video frames with the Core Animation layer.
- [AVVideoCompositionCoreAnimationTool.Configuration](./avvideocompositioncoreanimationtool/configuration.md)
  Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.
### Initializers
- [convenience init(postProcessingAsVideoLayer: CALayer, inLayer: CALayer)](./avvideocompositioncoreanimationtool/init%28postprocessingasvideolayer,inlayer%29.md)
- [convenience init(postProcessingAsVideoLayers: [CALayer], inLayer: CALayer)](./avvideocompositioncoreanimationtool/init%28postprocessingasvideolayers,inlayer%29.md)

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool)*