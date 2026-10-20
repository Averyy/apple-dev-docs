# removeFlagInBox(boundingBox:flag:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Removes the flag from all polygons in this box.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func removeFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)
```

## See Also

### Removing areas and flags
- [func removeAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](./removeareainbox%28boundingbox,area%29.md)
  Removes the area from all polygons in this box.
- [func removeAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)](./removeareaincylinder%28position,radius,halfheight,area%29.md)
  Removes the area from all polygons in this cylinder.
- [func removeFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](./removeflagincylinder%28position,radius,halfheight,flag%29.md)
  Removes the flag from all polygons in this cylinder.
- [func removeAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](./removeareaonpolygons%28polygonindices,area%29.md)
  Removes the area from the polygons at these indices.
- [func removeFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)](./removeflagonpolygons%28polygonindices,flag%29.md)
  Removes the flag from the polygons at these indices.
- [func removeAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](./removeareaonoffmeshconnections%28offmeshconnectionindices,area%29.md)
  Removes the area from the off-mesh connections at these indices.
- [func removeFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)](./removeflagonoffmeshconnections%28offmeshconnectionindices,flag%29.md)
  Removes the flag from the off-mesh connections at these indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/removeflaginbox(boundingbox:flag:))*