# init(node:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a component to manage the specified SpriteKit node.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(node: SKNode)
```

#### Return Value

A new SpriteKit component.

#### Discussion

When you add this component to a [`GKEntity`](gkentity.md) object, the component automatically sets the [`entity`](https://developer.apple.com/documentation/SpriteKit/SKNode/entity) property of its SpriteKit node to point to that entity.

## Parameters

- `node`: The SpriteKit node to be managed by the component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent/init(node:))*