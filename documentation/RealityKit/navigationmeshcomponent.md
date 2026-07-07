# NavigationMeshComponent

**Framework**: RealityKit  
**Kind**: struct

A component that provides the navigation meshes an entity uses to find paths through a scene.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NavigationMeshComponent
```

#### Overview

Attach a navigation mesh component to an entity to supply the walkable surfaces that pathfinding relies on. Each [`NavigationMeshResource`](navigationmeshresource.md) in [`navigationMeshes`](navigationmeshcomponent/navigationmeshes.md) represents a baked region of the scene that agents with a matching [`NavigationComponent`](navigationcomponent.md) can travel across.

## Topics

### Creating a navigation mesh component
- [init(navigationMeshes: [NavigationMeshResource])](navigationmeshcomponent/init(navigationmeshes:).md)
### Accessing the navigation meshes
- [var navigationMeshes: [NavigationMeshResource]](navigationmeshcomponent/navigationmeshes.md)
  The set of NavigationMeshResources.

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
- [struct NavigationComponent](navigationcomponent.md)
  A component that defines which areas of a navigation mesh an entity can move through.
- [struct NavigationController](navigationcontroller.md)
  An interface for finding paths for an entity moving across a scene’s navigation mesh.
- [class NavigationMeshResource](navigationmeshresource.md)
  A representation of a scene’s navigable surfaces that the system uses to compute paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshcomponent)*