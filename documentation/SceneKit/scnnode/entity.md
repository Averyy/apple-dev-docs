# entity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The GameplayKit entity this node represents.

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
weak var entity: GKEntity? { get set }
```

```objc
@property (nonatomic, weak) GKEntity * entity;
```

## Discussion

The Entity-Component architecture in the GameplayKit framework is a way to more easily manage complex object graphs in your game. For more information on this architecture, read [Entities and Components](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

When you add entities (and their components) to a scene in the Xcode SceneKit Scene Editor, Xcode automatically archive those entities alongside the SceneKit scene content. Use the [`GKScene`](../../GameplayKit/gkscene.md) class to load the SceneKit scene with its associated GameplayKit objects. Each entity associated with a SceneKit node has a [`GKSCNNodeComponent`](../../GameplayKit/gkscnnodecomponent.md) object that manages the relationship between the node and the [`GKEntity`](../../GameplayKit/gkentity.md) object it represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/entity)*