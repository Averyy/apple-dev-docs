# HasHierarchy

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

An interface that provides access to a parent entity and child entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency protocol HasHierarchy : Entity
```

## Mentions

- [Loading entities from a file](./loading-entities-from-a-file.md)

## Overview

All entities automatically adopt this protocol because the [`Entity`](./entity.md) base class does. This adoption gives all entities a collection of methods for managing the hierarchy.

## Topics

### Managing the parent
- [var parent: Entity?](./hashierarchy/parent.md)
  The parent entity.
- [func setParent(Entity?, preservingWorldTransform: Bool)](./hashierarchy/setparent%28_,preservingworldtransform%29.md)
  Attaches the entity as a child to the specified entity.
- [func removeFromParent(preservingWorldTransform: Bool)](./hashierarchy/removefromparent%28preservingworldtransform%29.md)
  Removes the entity from its current parent or from the scene if it is a root entity.
### Managing children
- [var children: Entity.ChildCollection](./hashierarchy/children.md)
  The child entities that the entity manages.
- [func addChild(Entity, preservingWorldTransform: Bool)](./hashierarchy/addchild%28_,preservingworldtransform%29.md)
  Adds the given entity to the collection of child entities.
- [func removeChild(Entity, preservingWorldTransform: Bool)](./hashierarchy/removechild%28_,preservingworldtransform%29.md)
  Removes the given child from the entity.

## Relationships

### Inherits From
- [Entity](./entity.md)
### Conforming Types
- [AnchorEntity](./anchorentity.md)
- [BodyTrackedEntity](./bodytrackedentity.md)
- [DirectionalLight](./directionallight.md)
- [Entity](./entity.md)
- [ModelEntity](./modelentity.md)
- [PerspectiveCamera](./perspectivecamera.md)
- [PointLight](./pointlight.md)
- [SpotLight](./spotlight.md)
- [TriggerVolume](./triggervolume.md)
- [ViewAttachmentEntity](./viewattachmententity.md)

## See Also

### Relating entities
- [var parameters: Entity.ParameterSet](./entity/parameters.md)
  Represents a reference to the parameters for a particular entity.
- [Entity.ChildCollection](./entity/childcollection.md)
  A collection of child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hashierarchy)*