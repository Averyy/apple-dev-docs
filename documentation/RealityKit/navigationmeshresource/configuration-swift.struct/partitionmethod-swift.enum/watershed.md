# NavigationMeshResource.Configuration.PartitionMethod.watershed

**Framework**: RealityKit  
**Kind**: case

The default method. Watershed is usually the slowest but creates the best-looking meshes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case watershed
```

## See Also

- [NavigationMeshResource.Configuration.PartitionMethod.monotone](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/monotone.md)
  The fastest method. On large, empty areas it tends to create long, thin polygons, so it is not ideal for generating the mesh offline or with large open regions in the geometry.
- [NavigationMeshResource.Configuration.PartitionMethod.layer](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/layer.md)
  A fast method, but slower than Monotone. It can create poor-looking meshes when used on large open regions, similar to Monotone, but will still generally create better-looking meshes than Monotone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/watershed)*