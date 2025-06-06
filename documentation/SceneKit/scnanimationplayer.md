# SCNAnimationPlayer

**Framework**: SceneKit  
**Kind**: class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class SCNAnimationPlayer
```

## Topics

### Initializers
- [init(animation: SCNAnimation)](scnanimationplayer/init(animation:).md)
### Instance Properties
- [var animation: SCNAnimation](scnanimationplayer/animation.md)
- [var blendFactor: CGFloat](scnanimationplayer/blendfactor.md)
- [var paused: Bool](scnanimationplayer/paused.md)
- [var speed: CGFloat](scnanimationplayer/speed.md)
### Instance Methods
- [func play()](scnanimationplayer/play.md)
- [func stop()](scnanimationplayer/stop.md)
- [func stop(withBlendOutDuration: TimeInterval)](scnanimationplayer/stop(withblendoutduration:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SCNAnimatable](scnanimatable.md)

## See Also

- [protocol SCNAnimatable](scnanimatable.md)
  The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.
- [class SCNAnimationEvent](scnanimationevent.md)
  A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.
- [class SCNAnimation](scnanimation-swift.class.md)
- [class SCNTimingFunction](scntimingfunction.md)
- [protocol SCNAnimationProtocol](scnanimationprotocol.md)
- [class SCNAnimation](scnanimation-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimationplayer)*