# markFlagOnOffMeshConnections(offMeshConnectionIndices:flag:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Marks the off-mesh connections at these indices with a flag.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func markFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)
```

## See Also

### Marking areas and flags
- [func markAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](./markareainbox%28boundingbox,area%29.md)
  Marks all polygons in this box with an area.
- [func markFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)](./markflaginbox%28boundingbox,flag%29.md)
  Marks all polygons in this box with a flag.
- [func markAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)](./markareaincylinder%28position,radius,halfheight,area%29.md)
  Marks all polygons in this cylinder with an area.
- [func markFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](./markflagincylinder%28position,radius,halfheight,flag%29.md)
  Marks all polygons in this cylinder with a flag.
- [func markAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](./markareaonpolygons%28polygonindices,area%29.md)
  Marks the polygons at these indices with an area.
- [func markFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)](./markflagonpolygons%28polygonindices,flag%29.md)
  Marks the polygons at these indices with a flag.
- [func markAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](./markareaonoffmeshconnections%28offmeshconnectionindices,area%29.md)
  Marks the off-mesh connections at these indices with an area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/markflagonoffmeshconnections(offmeshconnectionindices:flag:))*