# SCNAnimationEvent

**Framework**: SceneKit  
**Kind**: class

A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNAnimationEvent
```

#### Overview

Use animation events to add actions to animations, such as playing a sound to coincide with the movement of an animated character, or removing a node from the scene after playing an animation that fades out its visible geometry.

After you create an animation event, you attach it to an animation object using the object’s [`animationEvents`](https://developer.apple.com/documentation/QuartzCore/CAAnimation/animationEvents) property.

## Topics

### Creating an Animation Event
- [convenience init(keyTime: CGFloat, block: SCNAnimationEventBlock)](scnanimationevent/init(keytime:block:).md)
  Creates an animation event.
### Constants
- [typealias SCNAnimationEventBlock](scnanimationeventblock.md)
  Signature for the block called when an animation event triggers.

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

## See Also

- [protocol SCNAnimatable](scnanimatable.md)
  The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.
- [class SCNAnimation](scnanimation-swift.class.md)
- [class SCNAnimationPlayer](scnanimationplayer.md)
- [class SCNTimingFunction](scntimingfunction.md)
- [protocol SCNAnimationProtocol](scnanimationprotocol.md)
- [class SCNAnimation](scnanimation-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimationevent)*