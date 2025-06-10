# AVSynchronizedLayer

**Framework**: AVFoundation  
**Kind**: class

A Core Animation layer that derives its timing from a player item so that you can synchronize layer animations with media playback.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVSynchronizedLayer
```

#### Overview

You can create an arbitrary number of synchronized layers from the same `AVPlayerItem` object.

A synchronized layer is similar to a [`CATransformLayer`](https://developer.apple.com/documentation/QuartzCore/CATransformLayer) object in that it doesn’t display anything itself, it just confers state upon its layer subtree. `AVSynchronizedLayer` confers its timing state, synchronizing the timing of layers in its subtree with that of a player item.

Any `CoreAnimation` layer with animation property set that is added as a sublayer of `AVSynchronizedLayer` should set the animation’s [`beginTime`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/beginTime) property to a non-zero positive value so animations will be interpreted on the player item’s timeline. `CoreAnimation` replaces the default `beginTime` of 0.0 with [`CACurrentMediaTime()`](https://developer.apple.com/documentation/QuartzCore/CACurrentMediaTime()). To start the animation from time 0, use a small positive value like [`AVCoreAnimationBeginTimeAtZero`](avcoreanimationbegintimeatzero.md).

You might use a layer as shown in the following example:

```objc
AVPlayerItem *playerItem = <#Get a player item#>;
CALayer *superLayer =  <#Get a layer#>;
// Set up a synchronized layer to sync the layer timing of its subtree
// with the playback of the playerItem/
AVSynchronizedLayer *syncLayer = [AVSynchronizedLayer synchronizedLayerWithPlayerItem:playerItem];
[syncLayer addSublayer:<#Another layer#>];    // These sublayers will be synchronized.
[superLayer addSublayer:syncLayer];
```

## Topics

### Creating a Synchronized Layer
- [init(playerItem: AVPlayerItem)](avsynchronizedlayer/init(playeritem:).md)
  Creates a new synchronized layer with timing synchronized with a given player item.
### Managing the Player Item
- [var playerItem: AVPlayerItem?](avsynchronizedlayer/playeritem.md)
  The player item to which the timing of the layer is synchronized.
### Supporting Types
- [let AVCoreAnimationBeginTimeAtZero: CFTimeInterval](avcoreanimationbegintimeatzero.md)
  A value that sets an animation begin time to `0`.

## Relationships

### Inherits From
- [CALayer](../QuartzCore/CALayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/CAMediaTiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Monitoring playback progress in your app](monitoring-playback-progress-in-your-app.md)
  Observe the playback of a media asset to update your app’s user-interface state.
- [Using HEVC Video with Alpha](using-hevc-video-with-alpha.md)
  Play, write, and export HEVC video with an alpha channel to add overlay effects to your video processing.
- [class AVPlayerLayer](avplayerlayer.md)
  An object that presents the visual contents of a player object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer)*