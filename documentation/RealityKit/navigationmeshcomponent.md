# NavigationMeshComponent

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A component that provides the navigation meshes an entity uses to find paths through a scene.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct NavigationMeshComponent
```

## Overview

Attach a navigation mesh component to an entity to supply the walkable surfaces that pathfinding relies on. Each [`NavigationMeshResource`](./navigationmeshresource.md) in [`navigationMeshes`](./navigationmeshcomponent/navigationmeshes.md) represents a baked region of the scene that agents with a matching [`NavigationComponent`](./navigationcomponent.md) can travel across.

## Topics

### Creating a navigation mesh component
- [init(navigationMeshes: [NavigationMeshResource])](./navigationmeshcomponent/init%28navigationmeshes%29.md)
### Accessing the navigation meshes
- [var navigationMeshes: [NavigationMeshResource]](./navigationmeshcomponent/navigationmeshes.md)
  The set of NavigationMeshResources.

## Relationships

### Conforms To
- [Component](./component.md)

## See Also

### Navigation meshes
- [class NavigationMeshResource](./navigationmeshresource.md)
  A representation of a scene’s navigable surfaces that the system uses to compute paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshcomponent)*