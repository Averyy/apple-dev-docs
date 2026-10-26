# componentWithNode:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a component to manage the specified SpriteKit node.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) componentWithNode:(SKNode *) node;
```

#### Return Value

A new SpriteKit component.

#### Discussion

When you add this component to a [`GKEntity`](../gkentity.md) object, the component automatically sets the [`entity`](../../SpriteKit/sknode/entity.md) property of its SpriteKit node to point to that entity.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `node`: The SpriteKit node to be managed by the component.

## See Also

### Creating a SpriteKit Component
- [init(node: SKNode)](./init%28node%29.md)
  Initializes a component to manage the specified SpriteKit node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent/componentwithnode:)*