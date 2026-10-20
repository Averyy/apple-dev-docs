# SCNAnimationEvent

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.

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
class SCNAnimationEvent
```

```objc
@interface SCNAnimationEvent : NSObject
```

#### Overview

Use animation events to add actions to animations, such as playing a sound to coincide with the movement of an animated character, or removing a node from the scene after playing an animation that fades out its visible geometry.

After you create an animation event, you attach it to an animation object using the object’s [`animationEvents`](../QuartzCore/caanimation/animationevents.md) property.

## Topics

### Creating an Animation Event
- [convenience init(keyTime: CGFloat, block: SCNAnimationEventBlock)](./scnanimationevent/init%28keytime,block%29.md)
  Creates an animation event.
### Constants
- [typealias SCNAnimationEventBlock](./scnanimationeventblock.md)
  Signature for the block called when an animation event triggers.

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

## See Also

### Explicit Animation
- [protocol SCNAnimatable](./scnanimatable.md)
  The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.
- [class SCNAnimation](./scnanimation-swift.class.md)
- [class SCNAnimationPlayer](./scnanimationplayer.md)
- [class SCNTimingFunction](./scntimingfunction.md)
- [protocol SCNAnimationProtocol](./scnanimationprotocol.md)
- [class SCNAnimation](./scnanimation-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimationevent)*