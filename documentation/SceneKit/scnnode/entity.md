# entity

**Framework**: SceneKit  
**Kind**: property

The GameplayKit entity this node represents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var entity: GKEntity? { get set }
```

#### Discussion

The Entity-Component architecture in the GameplayKit framework is a way to more easily manage complex object graphs in your game. For more information on this architecture, read [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

When you add entities (and their components) to a scene in the Xcode SceneKit Scene Editor, Xcode automatically archive those entities alongside the SceneKit scene content. Use the [`GKScene`](https://developer.apple.com/documentation/GameplayKit/GKScene) class to load the SceneKit scene with its associated GameplayKit objects. Each entity associated with a SceneKit node has a [`GKSCNNodeComponent`](https://developer.apple.com/documentation/GameplayKit/GKSCNNodeComponent) object that manages the relationship between the node and the [`GKEntity`](https://developer.apple.com/documentation/GameplayKit/GKEntity) object it represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/entity)*