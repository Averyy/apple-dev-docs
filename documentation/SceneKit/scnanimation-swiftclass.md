# SCNAnimation

**Framework**: SceneKit  
**Kind**: class

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNAnimation
```

## Topics

### Supporting Types
- [typealias SCNAnimationDidStartBlock](scnanimationdidstartblock.md)
- [typealias SCNAnimationDidStopBlock](scnanimationdidstopblock.md)
### Initializers
- [init(CAAnimation: CAAnimation)](scnanimation-swift.class/init(caanimation:)-3sfjw.md)
- [init(caAnimation: CAAnimation)](scnanimation-swift.class/init(caanimation:)-4t0rw.md)
- [init?(coder: NSCoder)](scnanimation-swift.class/init(coder:).md)
- [init(contentsOf: URL)](scnanimation-swift.class/init(contentsof:).md)
- [init(contentsOfURL: URL)](scnanimation-swift.class/init(contentsofurl:).md)
- [init(named: String)](scnanimation-swift.class/init(named:).md)
### Instance Properties
- [var animationDidStart: SCNAnimationDidStartBlock?](scnanimation-swift.class/animationdidstart.md)
- [var animationDidStop: SCNAnimationDidStopBlock?](scnanimation-swift.class/animationdidstop.md)
- [var animationEvents: [SCNAnimationEvent]?](scnanimation-swift.class/animationevents.md)
- [var autoreverses: Bool](scnanimation-swift.class/autoreverses.md)
- [var blendInDuration: TimeInterval](scnanimation-swift.class/blendinduration.md)
- [var blendOutDuration: TimeInterval](scnanimation-swift.class/blendoutduration.md)
- [var duration: TimeInterval](scnanimation-swift.class/duration.md)
- [var fillsBackward: Bool](scnanimation-swift.class/fillsbackward.md)
- [var fillsForward: Bool](scnanimation-swift.class/fillsforward.md)
- [var isAdditive: Bool](scnanimation-swift.class/isadditive.md)
- [var isAppliedOnCompletion: Bool](scnanimation-swift.class/isappliedoncompletion.md)
- [var isCumulative: Bool](scnanimation-swift.class/iscumulative.md)
- [var isRemovedOnCompletion: Bool](scnanimation-swift.class/isremovedoncompletion.md)
- [var keyPath: String?](scnanimation-swift.class/keypath.md)
- [var repeatCount: CGFloat](scnanimation-swift.class/repeatcount.md)
- [var startDelay: TimeInterval](scnanimation-swift.class/startdelay.md)
- [var timeOffset: TimeInterval](scnanimation-swift.class/timeoffset.md)
- [var timingFunction: SCNTimingFunction](scnanimation-swift.class/timingfunction.md)
- [var usesSceneTimeBase: Bool](scnanimation-swift.class/usesscenetimebase.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [SCNAnimationProtocol](scnanimationprotocol.md)

## See Also

- [protocol SCNAnimatable](scnanimatable.md)
  The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.
- [class SCNAnimationEvent](scnanimationevent.md)
  A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.
- [class SCNAnimationPlayer](scnanimationplayer.md)
- [class SCNTimingFunction](scntimingfunction.md)
- [protocol SCNAnimationProtocol](scnanimationprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimation-swift.class)*