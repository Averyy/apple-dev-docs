# NavigationMeshResource.FlagGroup

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of Flags.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct FlagGroup
```

## Topics

### Modifying flags
- [func setFlag(NavigationMeshResource.Flag)](./flaggroup/setflag%28_%29.md)
  Sets a specific flag in the [`NavigationMeshResource.FlagGroup`](./flaggroup.md).
- [func unsetFlag(NavigationMeshResource.Flag)](./flaggroup/unsetflag%28_%29.md)
  Unsets a specific flag in the [`NavigationMeshResource.FlagGroup`](./flaggroup.md).
### Initializers
- [init(UInt64)](./flaggroup/init%28_%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Supporting types
- [NavigationMeshResource.Configuration](./configuration-swift.struct.md)
  The NavigationMeshResource configuration that defines how the mesh is created.
- [NavigationMeshResource.Area](./area.md)
  An identifier for different areas on a Navigation Mesh.
- [NavigationMeshResource.Flag](./flag.md)
  An identifier for different flags on a Navigation Mesh.
- [NavigationMeshResource.OffMeshConnection](./offmeshconnection.md)
  A container for the data associated with an off-mesh connection.
- [NavigationMeshResource.HeightData](./heightdata-swift.struct.md)
  A container for the detailed height data of the NavigationMeshResource.
- [NavigationMeshResource.Layer](./layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](../navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.
- [NavigationMeshResource.PathNode](./pathnode.md)
  A container for the path node data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/flaggroup)*