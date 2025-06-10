# AVVideoCompositionCoreAnimationTool

**Framework**: AVFoundation  
**Kind**: class

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

#### Overview

Any animations will be interpreted on the video’s timeline, not real-time, so you should:

1. Set animations’ [`beginTime`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/beginTime) property to [`AVCoreAnimationBeginTimeAtZero`](avcoreanimationbegintimeatzero.md) rather than `0` (which CoreAnimation replaces with [`CACurrentMediaTime()`](https://developer.apple.com/documentation/QuartzCore/CACurrentMediaTime()));
2. Set [`isRemovedOnCompletion`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/isRemovedOnCompletion) to [`false`](https://developer.apple.com/documentation/swift/false) on animations so they are not automatically removed;
3. Avoid using layers that are associated with [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) objects.

## Topics

### Creating a Composition Tool
- [convenience init(additionalLayer: sending CALayer, asTrackID: CMPersistentTrackID)](avvideocompositioncoreanimationtool/init(additionallayer:astrackid:).md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayer: CALayer, in: CALayer)](avvideocompositioncoreanimationtool/init(postprocessingasvideolayer:in:).md)
  Composes the composited video frame with a Core Animation layer.
- [convenience init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](avvideocompositioncoreanimationtool/init(postprocessingasvideolayers:in:).md)
  Composes the composited video frames with the Core Animation layer.
### Structures
- [AVVideoCompositionCoreAnimationTool.Configuration](avvideocompositioncoreanimationtool/configuration.md)
  Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.
### Initializers
- [convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)](avvideocompositioncoreanimationtool/init(configuration:).md)
  Compose the composited video frames with the Core Animation layer.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool)*