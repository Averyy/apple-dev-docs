# NavigationMeshResource.FlagGroup

**Framework**: RealityKit  
**Kind**: struct

A collection of Flags.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FlagGroup
```

## Topics

### Modifying flags
- [func setFlag(NavigationMeshResource.Flag)](navigationmeshresource/flaggroup/setflag(_:).md)
  Sets a specific flag in the [`NavigationMeshResource.FlagGroup`](navigationmeshresource/flaggroup.md).
- [func unsetFlag(NavigationMeshResource.Flag)](navigationmeshresource/flaggroup/unsetflag(_:).md)
  Unsets a specific flag in the [`NavigationMeshResource.FlagGroup`](navigationmeshresource/flaggroup.md).
### Initializers
- [init(UInt64)](navigationmeshresource/flaggroup/init(_:).md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [NavigationMeshResource.Configuration](navigationmeshresource/configuration-swift.struct.md)
  The NavigationMeshResource configuration that defines how the mesh is created.
- [NavigationMeshResource.Area](navigationmeshresource/area.md)
  An identifier for different areas on a Navigation Mesh.
- [NavigationMeshResource.Flag](navigationmeshresource/flag.md)
  An identifier for different flags on a Navigation Mesh.
- [NavigationMeshResource.OffMeshConnection](navigationmeshresource/offmeshconnection.md)
  A container for the data associated with an off-mesh connection.
- [NavigationMeshResource.HeightData](navigationmeshresource/heightdata-swift.struct.md)
  A container for the detailed height data of the NavigationMeshResource.
- [NavigationMeshResource.Layer](navigationmeshresource/layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.
- [NavigationMeshResource.PathNode](navigationmeshresource/pathnode.md)
  A container for the path node data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/flaggroup)*