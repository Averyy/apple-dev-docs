# GKSceneRootNodeType

**Framework**: GameplayKit  
**Kind**: protocol

Identifies scene classes from other frameworks that support embedded GameplayKit information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKSceneRootNodeType : NSObjectProtocol
```

#### Overview

You do not define classes that adopt this protocol. GameplayKit adds this protocol declaration to classes (such as [`SKScene`](https://developer.apple.com/documentation/SpriteKit/SKScene)) for which the [`GKScene`](gkscene.md) class supports archiving and loading embedded GameplayKit information.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKScene](gkscene.md)
  A container for associating GameplayKit objects with a SpriteKit scene.
- [class GKSKNodeComponent](gksknodecomponent.md)
  A component that manages a SpriteKit node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkscenerootnodetype)*