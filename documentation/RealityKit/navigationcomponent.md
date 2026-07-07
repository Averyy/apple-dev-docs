# NavigationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines which areas of a navigation mesh an entity can move through.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NavigationComponent
```

#### Overview

Add a navigation component to an entity to make it a navigation agent. Its [`layer`](navigationcomponent/layer.md) selects the navigation mesh the entity travels on, and its [`filter`](navigationcomponent/filter-swift.property.md) restricts which marked areas the entity can cross when a [`NavigationController`](navigationcontroller.md) finds a path.

## Topics

### Creating a component
- [init(layer: NavigationMeshResource.Layer?, filter: NavigationComponent.Filter?)](navigationcomponent/init(layer:filter:).md)
### Configuring navigation
- [var layer: NavigationMeshResource.Layer?](navigationcomponent/layer.md)
  The layer to use when searching for a NavigationMeshResource in a Scene. If not set, the first available NavigationMeshResource will be used.
- [var filter: NavigationComponent.Filter?](navigationcomponent/filter-swift.property.md)
  The filter to use when pathfinding.
- [NavigationComponent.Filter](navigationcomponent/filter-swift.struct.md)
  A struct that stores information about flags to ignore and include, and area costs for a pathfind.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [Gaming sample code projects](game-development-sample-code.md)
  Explore a collection of projects relating to game development.
- [Entity animations](game-development-entity-animations.md)
  Dynamically move, rotate, and scale entities at runtime.
- [Character control, skeletons, and inverse kinematics](game-development-character-skeletons.md)
  Direct the movements and animation of models.
- [struct NavigationMeshComponent](navigationmeshcomponent.md)
  A component that provides the navigation meshes an entity uses to find paths through a scene.
- [struct NavigationController](navigationcontroller.md)
  An interface for finding paths for an entity moving across a scene’s navigation mesh.
- [class NavigationMeshResource](navigationmeshresource.md)
  A representation of a scene’s navigable surfaces that the system uses to compute paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcomponent)*