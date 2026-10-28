# SKAction

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

An object that is run by a node to change its structure or content.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class SKAction
```

```objc
@interface SKAction : NSObject
```

## Mentions

- [Getting Started with Actions](./getting-started-with-actions.md)
- [Getting Started with Spring Joints](./getting-started-with-spring-joints.md)
- [Working with Inverse Kinematics](./working-with-inverse-kinematics.md)

## Overview

[`SKAction`](./skaction.md) is an animation that is executed by a node in the scene. Actions are used to change a node in some way (like move its position over time), but you can also use actions to change the scene, like doing a fadeout. When the scene processes its nodes, the actions associated with those nodes are processed.

## Topics

### First Steps
- [Getting Started with Actions](./getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.
- [Action Initializers](./action-initializers.md)
  Use these functions to create actions.
### Controlling Action Timing
- [Configuring Action Timing](./configuring-action-timing.md)
  Time an action in a scene, by adding or modifying timing properties, or cancel an action.
- [var duration: TimeInterval](./skaction/duration.md)
  The duration required to complete an action.
- [var timingMode: SKActionTimingMode](./skaction/timingmode.md)
  A setting that controls the speed curve of an animation.
- [enum SKActionTimingMode](./skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [var timingFunction: SKActionTimingFunction](./skaction/timingfunction.md)
  A block used to customize the timing function.
- [typealias SKActionTimingFunction](./skactiontimingfunction.md)
  The signature for the custom timing block.
- [var speed: CGFloat](./skaction/speed.md)
  A speed factor that modifies how fast an action runs.
### Using Action Names
- [Controlling Actions Precisely by Using Names](./controlling-actions-precisely-by-using-names.md)
  Set an action’s name property so you can access it later without needing an instance variable.
### Observing Live Changes
- [Detecting Changes at Each Step of an Animation](./detecting-changes-at-each-step-of-an-animation.md)
  Get notified of a property change on your node subclass and retrieve the amount of change.
### Initializers
- [init?(coder: NSCoder)](./skaction/init%28coder%29.md)
- [init?(named: String, from: URL)](./skaction/init%28named,from%29.md)
  Creates an action of the given name from an action file.
- [init?(named: String, from: URL, duration: TimeInterval)](./skaction/init%28named,from,duration%29.md)
  Creates an action of the given name from an action file with a new duration.
### Default Implementations
- [SKAction Implementations](./skaction/skaction-implementations.md)

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

## See Also

### Animation
- [Getting Started with Actions](./getting-started-with-actions.md)
  Create, configure, and run actions in SpriteKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction)*