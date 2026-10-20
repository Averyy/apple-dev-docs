# NavigationController.PathfindStatus

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The status of a pathfinding request.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum PathfindStatus
```

## Topics

### Reading the pathfinding status
- [NavigationController.PathfindStatus.inProgress](./pathfindstatus-swift.enum/inprogress.md)
  The pathfind is still running and has not completed.
- [NavigationController.PathfindStatus.succeeded](./pathfindstatus-swift.enum/succeeded.md)
  The pathfind succeeded in finding a path.
- [NavigationController.PathfindStatus.failed](./pathfindstatus-swift.enum/failed.md)
  The pathfind failed to run or find a path.
- [NavigationController.PathfindStatus.none](./pathfindstatus-swift.enum/none.md)
  No pathfind request was made or any existing ones were cancelled.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Monitoring pathfinding status
- [var pathfindStatus: NavigationController.PathfindStatus](./pathfindstatus-swift.property.md)
  The current pathfind status.
- [var currentPath: [NavigationMeshResource.PathNode]](./currentpath.md)
  The computed path to the target position found by requestPath(). If called before the pathfind completes, a partial path will be returned. This partial path may be suboptimal. If the pathfind failed or was not requested, the function will return an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcontroller/pathfindstatus-swift.enum)*