# NavigationController

**Framework**: RealityKit  
**Kind**: struct

An interface for finding paths for an entity moving across a scene’s navigation mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NavigationController
```

#### Overview

Create a navigation controller for an entity, then call [`requestPath(to:)`](navigationcontroller/requestpath(to:).md) to start an asynchronous pathfind or [`computePath(to:)`](navigationcontroller/computepath(to:).md) to compute a path immediately. Track [`pathfindStatus`](navigationcontroller/pathfindstatus-swift.property.md) and read [`currentPath`](navigationcontroller/currentpath.md) to follow the result.

## Topics

### Creating a navigation controller
- [init(entity: Entity) throws](navigationcontroller/init(entity:).md)
  Creates a NavigationController from an Entity with a NavigationComponent.
### Requesting pathfinding
- [func requestPath(to: SIMD3<Float>)](navigationcontroller/requestpath(to:).md)
  Requests a pathfind from the owning entity’s position to the target position.
- [func requestPath(from: SIMD3<Float>, to: SIMD3<Float>)](navigationcontroller/requestpath(from:to:).md)
  Requests a pathfind from a given position to the target position.
- [func stopPathfind()](navigationcontroller/stoppathfind.md)
  Cancels any in-progress pathfinds.
### Computing paths
- [func computePath(to: SIMD3<Float>) async -> [NavigationMeshResource.PathNode]?](navigationcontroller/computepath(to:).md)
  Asynchronously requests a pathfind from the owning entity’s position to the target position and waits for the path or a failure. If the function returns an empty path, the pathfind succeeded with no nodes (for example, the start and end positions are in the same place). If the function returns nil, the pathfinding failed to find a path.
- [func computePath(from: SIMD3<Float>, to: SIMD3<Float>) async -> [NavigationMeshResource.PathNode]?](navigationcontroller/computepath(from:to:).md)
  Asynchronously requests a pathfind from a given position to the target position and waits for the path or a failure. If the function returns an empty path, the pathfind succeeded with no nodes (for example, the start and end positions are in the same place). If the function returns nil, the pathfinding failed to find a path.
### Monitoring pathfinding status
- [var pathfindStatus: NavigationController.PathfindStatus](navigationcontroller/pathfindstatus-swift.property.md)
  The current pathfind status.
- [NavigationController.PathfindStatus](navigationcontroller/pathfindstatus-swift.enum.md)
  The status of a pathfinding request.
- [var currentPath: [NavigationMeshResource.PathNode]](navigationcontroller/currentpath.md)
  The computed path to the target position found by requestPath(). If called before the pathfind completes, a partial path will be returned. This partial path may be suboptimal. If the pathfind failed or was not requested, the function will return an empty array.

## See Also

- [Gaming sample code projects](game-development-sample-code.md)
  Explore a collection of projects relating to game development.
- [Entity animations](game-development-entity-animations.md)
  Dynamically move, rotate, and scale entities at runtime.
- [Character control, skeletons, and inverse kinematics](game-development-character-skeletons.md)
  Direct the movements and animation of models.
- [struct NavigationComponent](navigationcomponent.md)
  A component that defines which areas of a navigation mesh an entity can move through.
- [struct NavigationMeshComponent](navigationmeshcomponent.md)
  A component that provides the navigation meshes an entity uses to find paths through a scene.
- [class NavigationMeshResource](navigationmeshresource.md)
  A representation of a scene’s navigable surfaces that the system uses to compute paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcontroller)*