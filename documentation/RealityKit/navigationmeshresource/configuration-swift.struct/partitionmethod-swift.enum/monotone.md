# NavigationMeshResource.Configuration.PartitionMethod.monotone

**Framework**: RealityKit  
**Kind**: case

The fastest method. On large, empty areas it tends to create long, thin polygons, so it is not ideal for generating the mesh offline or with large open regions in the geometry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case monotone
```

## See Also

- [NavigationMeshResource.Configuration.PartitionMethod.watershed](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/watershed.md)
  The default method. Watershed is usually the slowest but creates the best-looking meshes.
- [NavigationMeshResource.Configuration.PartitionMethod.layer](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/layer.md)
  A fast method, but slower than Monotone. It can create poor-looking meshes when used on large open regions, similar to Monotone, but will still generally create better-looking meshes than Monotone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/monotone)*