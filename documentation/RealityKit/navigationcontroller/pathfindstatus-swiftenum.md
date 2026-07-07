# NavigationController.PathfindStatus

**Framework**: RealityKit  
**Kind**: enum

The status of a pathfinding request.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum PathfindStatus
```

## Topics

### Reading the pathfinding status
- [NavigationController.PathfindStatus.inProgress](navigationcontroller/pathfindstatus-swift.enum/inprogress.md)
  The pathfind is still running and has not completed.
- [NavigationController.PathfindStatus.succeeded](navigationcontroller/pathfindstatus-swift.enum/succeeded.md)
  The pathfind succeeded in finding a path.
- [NavigationController.PathfindStatus.failed](navigationcontroller/pathfindstatus-swift.enum/failed.md)
  The pathfind failed to run or find a path.
- [NavigationController.PathfindStatus.none](navigationcontroller/pathfindstatus-swift.enum/none.md)
  No pathfind request was made or any existing ones were cancelled.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var pathfindStatus: NavigationController.PathfindStatus](navigationcontroller/pathfindstatus-swift.property.md)
  The current pathfind status.
- [var currentPath: [NavigationMeshResource.PathNode]](navigationcontroller/currentpath.md)
  The computed path to the target position found by requestPath(). If called before the pathfind completes, a partial path will be returned. This partial path may be suboptimal. If the pathfind failed or was not requested, the function will return an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcontroller/pathfindstatus-swift.enum)*