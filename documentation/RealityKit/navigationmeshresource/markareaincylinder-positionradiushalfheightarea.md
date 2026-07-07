# markAreaInCylinder(position:radius:halfHeight:area:)

**Framework**: RealityKit  
**Kind**: method

Marks all polygons in this cylinder with an area.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func markAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)
```

## See Also

- [func markAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](navigationmeshresource/markareainbox(boundingbox:area:).md)
  Marks all polygons in this box with an area.
- [func markFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)](navigationmeshresource/markflaginbox(boundingbox:flag:).md)
  Marks all polygons in this box with a flag.
- [func markFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](navigationmeshresource/markflagincylinder(position:radius:halfheight:flag:).md)
  Marks all polygons in this cylinder with a flag.
- [func markAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/markareaonpolygons(polygonindices:area:).md)
  Marks the polygons at these indices with an area.
- [func markFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)](navigationmeshresource/markflagonpolygons(polygonindices:flag:).md)
  Marks the polygons at these indices with a flag.
- [func markAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/markareaonoffmeshconnections(offmeshconnectionindices:area:).md)
  Marks the off-mesh connections at these indices with an area.
- [func markFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)](navigationmeshresource/markflagonoffmeshconnections(offmeshconnectionindices:flag:).md)
  Marks the off-mesh connections at these indices with a flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/markareaincylinder(position:radius:halfheight:area:))*