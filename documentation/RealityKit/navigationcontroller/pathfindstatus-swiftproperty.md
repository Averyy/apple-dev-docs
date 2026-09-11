# pathfindStatus

**Framework**: RealityKit  
**Kind**: property

The current pathfind status.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var pathfindStatus: NavigationController.PathfindStatus { get }
```

## See Also

- [NavigationController.PathfindStatus](navigationcontroller/pathfindstatus-swift.enum.md)
  The status of a pathfinding request.
- [var currentPath: [NavigationMeshResource.PathNode]](navigationcontroller/currentpath.md)
  The computed path to the target position found by requestPath(). If called before the pathfind completes, a partial path will be returned. This partial path may be suboptimal. If the pathfind failed or was not requested, the function will return an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcontroller/pathfindstatus-swift.property)*