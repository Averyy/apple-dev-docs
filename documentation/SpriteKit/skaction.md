# SKAction

**Framework**: SpriteKit  
**Kind**: class

An object that is run by a node to change its structure or content.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SKAction
```

## Mentions

- [Working with Inverse Kinematics](working-with-inverse-kinematics.md)
- [Getting Started with Spring Joints](getting-started-with-spring-joints.md)
- [Getting Started with Actions](getting-started-with-actions.md)

#### Overview

[`SKAction`](skaction.md) is an animation that is executed by a node in the scene. Actions are used to change a node in some way (like move its position over time), but you can also use actions to change the scene, like doing a fadeout. When the scene processes its nodes, the actions associated with those nodes are processed.

## Topics

### First Steps
- [Getting Started with Actions](getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [Action Initializers](action-initializers.md)
  Use these functions to create actions.
### Controlling Action Timing
- [Configuring Action Timing](configuring-action-timing.md)
  Time an action in a scene, by adding or modifying timing properties, or cancel an action.
- [var duration: TimeInterval](skaction/duration.md)
  The duration required to complete an action.
- [var timingMode: SKActionTimingMode](skaction/timingmode.md)
  A setting that controls the speed curve of an animation.
- [enum SKActionTimingMode](skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [var timingFunction: SKActionTimingFunction](skaction/timingfunction.md)
  A block used to customize the timing function.
- [typealias SKActionTimingFunction](skactiontimingfunction.md)
  The signature for the custom timing block.
- [var speed: CGFloat](skaction/speed.md)
  A speed factor that modifies how fast an action runs.
### Using Action Names
- [Controlling Actions Precisely by Using Names](controlling-actions-precisely-by-using-names.md)
  Set an action’s name property so you can access it later without needing an instance variable.
### Observing Live Changes
- [Detecting Changes at Each Step of an Animation](detecting-changes-at-each-step-of-an-animation.md)
  Get notified of a property change on your node subclass and retrieve the amount of change.

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

## See Also

- [Getting Started with Actions](getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction)*