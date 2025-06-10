# GKScene

**Framework**: GameplayKit  
**Kind**: class

A container for associating GameplayKit objects with a SpriteKit scene.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKScene
```

#### Overview

When you create a scene in the Xcode SpriteKit scene editor, Xcode automatically creates a [`GKScene`](gkscene.md) object to manage any GameplayKit objects you add to the scene (entities, components, or pathfinding graphs) and archive them alongside the SpriteKit scene content.

To use a SpriteKit scene that contains GameplayKit objects, load the scene file with the [`GKScene`](gkscene.md) [`init(fileNamed:)`](gkscene/init(filenamed:).md) method. You can then use the [`entities`](gkscene/entities.md) and [`graphs`](gkscene/graphs.md) properties to access the [`GKEntity`](gkentity.md) (and associated [`GKComponent`](gkcomponent.md)) objects and [`GKGraph`](gkgraph.md) objects in the scene, and the [`rootNode`](gkscene/rootnode.md) property to access the scene’s SpriteKit content.

> **Note**:  Any SpriteKit node in the scene to which you’ve attached an entity or components automatically has a [`GKSKNodeComponent`](gksknodecomponent.md) object to manage the relationship between the node and the the [`GKEntity`](gkentity.md) object it represents.

For more information on Entity-Component architecture and pathfinding graphs, see [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) and [`Pathfinding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Pathfinding.html#//apple_ref/doc/uid/TP40015172-CH3) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Loading a Scene File
- [convenience init?(fileNamed: String)](gkscene/init(filenamed:).md)
  Loads the specified SpriteKit scene file, creating a [`GKScene`](gkscene.md) object containing the SpriteKit scene and associated GameplayKit objects.
### Accessing the SpriteKit Scene
- [var rootNode: (any GKSceneRootNodeType)?](gkscene/rootnode.md)
  The SpriteKit scene managed by this [`GKScene`](gkscene.md) object.
### Managing Entities and Components
- [var entities: [GKEntity]](gkscene/entities.md)
  The list of GameplayKit entities managed by the scene.
- [func addEntity(GKEntity)](gkscene/addentity(_:).md)
  Adds a GameplayKit entity to the list of entities managed by the scene.
- [func removeEntity(GKEntity)](gkscene/removeentity(_:).md)
  Removes a GameplayKit entity from the list of entities managed by the scene.
### Managing Pathfinding Graphs
- [var graphs: [String : GKGraph]](gkscene/graphs.md)
  The list of pathfinding graph objects managed by the scene.
- [func removeGraph(String)](gkscene/removegraph(_:).md)
  Removes a pathfinding graph from the list of graphs managed by the scene.
### Initializers
- [convenience init?(fileNamed: String, rootNode: any GKSceneRootNodeType)](gkscene/init(filenamed:rootnode:).md)
### Instance Methods
- [func addGraph(GKGraph, name: String)](gkscene/addgraph(_:name:).md)

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

- [protocol GKSceneRootNodeType](gkscenerootnodetype.md)
  Identifies scene classes from other frameworks that support embedded GameplayKit information.
- [class GKSKNodeComponent](gksknodecomponent.md)
  A component that manages a SpriteKit node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkscene)*