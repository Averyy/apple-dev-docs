# NavigationComponent.Filter

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A struct that stores information about flags to ignore and include, and area costs for a pathfind.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Filter
```

## Topics

### Configuring the filter
- [var includeFlags: NavigationMeshResource.FlagGroup](./filter-swift.struct/includeflags.md)
  The set of flags to include when pathfinding. The path will only move through polygons that have any of these flags set.
- [var ignoreFlags: NavigationMeshResource.FlagGroup](./filter-swift.struct/ignoreflags.md)
  The set of flags to ignore when pathfinding. The path will not be able to move through any polygons with any of these flags set.
- [var areaCosts: [NavigationMeshResource.Area : Float]](./filter-swift.struct/areacosts.md)
  The costs for pathing through an area. The path can move through polygons with these areas, but will try to find the lowest-cost path, avoiding high-cost areas if possible.
### Initializers
- [init()](./filter-swift.struct/init%28%29.md)

## See Also

### Configuring navigation
- [var layer: NavigationMeshResource.Layer?](./layer.md)
  The layer to use when searching for a NavigationMeshResource in a Scene. If not set, the first available NavigationMeshResource will be used.
- [var filter: NavigationComponent.Filter?](./filter-swift.property.md)
  The filter to use when pathfinding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationcomponent/filter-swift.struct)*