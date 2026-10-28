# node

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong) SKNode * node;
```

## Discussion

When you add this component to a [`GKEntity`](../gkentity.md) object, the component automatically sets the [`entity`](../../SpriteKit/sknode/entity.md) property of its SpriteKit node to point to that entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent/node)*