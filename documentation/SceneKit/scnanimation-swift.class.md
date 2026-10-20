# SCNAnimation

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class SCNAnimation
```

```objc
@interface SCNAnimation : NSObject
```

## Topics

### Supporting Types
- [typealias SCNAnimationDidStartBlock](./scnanimationdidstartblock.md)
- [typealias SCNAnimationDidStopBlock](./scnanimationdidstopblock.md)
### Initializers
- [init(CAAnimation: CAAnimation)](./scnanimation-swift.class/init%28caanimation%29-3sfjw.md)
- [init(caAnimation: CAAnimation)](./scnanimation-swift.class/init%28caanimation%29-4t0rw.md)
- [init?(coder: NSCoder)](./scnanimation-swift.class/init%28coder%29.md)
- [init(contentsOf: URL)](./scnanimation-swift.class/init%28contentsof%29.md)
- [init(contentsOfURL: URL)](./scnanimation-swift.class/init%28contentsofurl%29.md)
- [init(named: String)](./scnanimation-swift.class/init%28named%29.md)
### Instance Properties
- [var animationDidStart: SCNAnimationDidStartBlock?](./scnanimation-swift.class/animationdidstart.md)
- [var animationDidStop: SCNAnimationDidStopBlock?](./scnanimation-swift.class/animationdidstop.md)
- [var animationEvents: [SCNAnimationEvent]?](./scnanimation-swift.class/animationevents.md)
- [var autoreverses: Bool](./scnanimation-swift.class/autoreverses.md)
- [var blendInDuration: TimeInterval](./scnanimation-swift.class/blendinduration.md)
- [var blendOutDuration: TimeInterval](./scnanimation-swift.class/blendoutduration.md)
- [var duration: TimeInterval](./scnanimation-swift.class/duration.md)
- [var fillsBackward: Bool](./scnanimation-swift.class/fillsbackward.md)
- [var fillsForward: Bool](./scnanimation-swift.class/fillsforward.md)
- [var isAdditive: Bool](./scnanimation-swift.class/isadditive.md)
- [var isAppliedOnCompletion: Bool](./scnanimation-swift.class/isappliedoncompletion.md)
- [var isCumulative: Bool](./scnanimation-swift.class/iscumulative.md)
- [var isRemovedOnCompletion: Bool](./scnanimation-swift.class/isremovedoncompletion.md)
- [var keyPath: String?](./scnanimation-swift.class/keypath.md)
- [var repeatCount: CGFloat](./scnanimation-swift.class/repeatcount.md)
- [var startDelay: TimeInterval](./scnanimation-swift.class/startdelay.md)
- [var timeOffset: TimeInterval](./scnanimation-swift.class/timeoffset.md)
- [var timingFunction: SCNTimingFunction](./scnanimation-swift.class/timingfunction.md)
- [var usesSceneTimeBase: Bool](./scnanimation-swift.class/usesscenetimebase.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [SCNAnimationProtocol](./scnanimationprotocol.md)

## See Also

### Explicit Animation
- [protocol SCNAnimatable](./scnanimatable.md)
  The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.
- [class SCNAnimationEvent](./scnanimationevent.md)
  A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.
- [class SCNAnimationPlayer](./scnanimationplayer.md)
- [class SCNTimingFunction](./scntimingfunction.md)
- [protocol SCNAnimationProtocol](./scnanimationprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimation-swift.class)*