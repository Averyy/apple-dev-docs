# currentPath

**Framework**: RealityKit  
**Kind**: property

The computed path to the target position found by requestPath(). If called before the pathfind completes, a partial path will be returned. This partial path may be suboptimal. If the pathfind failed or was not requested, the function will return an empty array.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var currentPath: [NavigationMeshResource.PathNode] { get }
```

## See Also

- [var pathfindStatus: NavigationController.PathfindStatus](navigationcontroller/pathfindstatus-swift.property.md)
  The current pathfind status.
- [NavigationController.PathfindStatus](navigationcontroller/pathfindstatus-swift.enum.md)
  The status of a pathfinding request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcontroller/currentpath)*