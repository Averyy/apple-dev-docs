# SCNAnimationPlayer

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
class SCNAnimationPlayer
```

## Topics

### Initializers
- [init(animation: SCNAnimation)](scnanimationplayer/init(animation:).md)
- [init?(coder: NSCoder)](scnanimationplayer/init(coder:).md)
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