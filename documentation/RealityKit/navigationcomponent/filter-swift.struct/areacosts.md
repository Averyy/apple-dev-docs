# areaCosts

**Framework**: RealityKit  
**Kind**: property

The costs for pathing through an area. The path can move through polygons with these areas, but will try to find the lowest-cost path, avoiding high-cost areas if possible.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var areaCosts: [NavigationMeshResource.Area : Float]
```

## See Also

- [var includeFlags: NavigationMeshResource.FlagGroup](navigationcomponent/filter-swift.struct/includeflags.md)
  The set of flags to include when pathfinding. The path will only move through polygons that have any of these flags set.
- [var ignoreFlags: NavigationMeshResource.FlagGroup](navigationcomponent/filter-swift.struct/ignoreflags.md)
  The set of flags to ignore when pathfinding. The path will not be able to move through any polygons with any of these flags set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcomponent/filter-swift.struct/areacosts)*