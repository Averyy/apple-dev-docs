# SCNAnimationPlayer

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
class SCNAnimationPlayer
```

```objc
@interface SCNAnimationPlayer : NSObject
```

## Topics

### Initializers
- [init(animation: SCNAnimation)](./scnanimationplayer/init%28animation%29.md)
- [init?(coder: NSCoder)](./scnanimationplayer/init%28coder%29.md)
### Instance Properties
- [var animation: SCNAnimation](./scnanimationplayer/animation.md)
- [var blendFactor: CGFloat](./scnanimationplayer/blendfactor.md)
- [var paused: Bool](./scnanimationplayer/paused.md)
- [var speed: CGFloat](./scnanimationplayer/speed.md)
### Instance Methods
- [func play()](./scnanimationplayer/play%28%29.md)
- [func stop()](./scnanimationplayer/stop%28%29.md)
- [func stop(withBlendOutDuration: TimeInterval)](./scnanimationplayer/stop%28withblendoutduration%29.md)

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
- [SCNAnimatable](./scnanimatable.md)

## See Also

### Explicit Animation
- [protocol SCNAnimatable](./scnanimatable.md)
  The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.
- [class SCNAnimationEvent](./scnanimationevent.md)
  A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.
- [class SCNAnimation](./scnanimation-swift.class.md)
- [class SCNTimingFunction](./scntimingfunction.md)
- [protocol SCNAnimationProtocol](./scnanimationprotocol.md)
- [class SCNAnimation](./scnanimation-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimationplayer)*