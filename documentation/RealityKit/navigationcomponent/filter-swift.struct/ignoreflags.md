# ignoreFlags

**Framework**: RealityKit  
**Kind**: property

The set of flags to ignore when pathfinding. The path will not be able to move through any polygons with any of these flags set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var ignoreFlags: NavigationMeshResource.FlagGroup
```

## See Also

- [var includeFlags: NavigationMeshResource.FlagGroup](navigationcomponent/filter-swift.struct/includeflags.md)
  The set of flags to include when pathfinding. The path will only move through polygons that have any of these flags set.
- [var areaCosts: [NavigationMeshResource.Area : Float]](navigationcomponent/filter-swift.struct/areacosts.md)
  The costs for pathing through an area. The path can move through polygons with these areas, but will try to find the lowest-cost path, avoiding high-cost areas if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcomponent/filter-swift.struct/ignoreflags)*