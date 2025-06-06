# node

**Framework**: GameplayKit  
**Kind**: property

The SpriteKit node managed by the component.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var node: SKNode { get set }
```

#### Discussion

When you add this component to a [`GKEntity`](gkentity.md) object, the component automatically sets the [`entity`](https://developer.apple.com/documentation/SpriteKit/SKNode/entity) property of its SpriteKit node to point to that entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent/node)*