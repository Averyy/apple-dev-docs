# removeFlagOnPolygons(polygonIndices:flag:)

**Framework**: RealityKit  
**Kind**: method

Removes the flag from the polygons at these indices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func removeFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)
```

## See Also

- [func removeAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](navigationmeshresource/removeareainbox(boundingbox:area:).md)
  Removes the area from all polygons in this box.
- [func removeFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)](navigationmeshresource/removeflaginbox(boundingbox:flag:).md)
  Removes the flag from all polygons in this box.
- [func removeAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)](navigationmeshresource/removeareaincylinder(position:radius:halfheight:area:).md)
  Removes the area from all polygons in this cylinder.
- [func removeFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](navigationmeshresource/removeflagincylinder(position:radius:halfheight:flag:).md)
  Removes the flag from all polygons in this cylinder.
- [func removeAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/removeareaonpolygons(polygonindices:area:).md)
  Removes the area from the polygons at these indices.
- [func removeAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/removeareaonoffmeshconnections(offmeshconnectionindices:area:).md)
  Removes the area from the off-mesh connections at these indices.
- [func removeFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)](navigationmeshresource/removeflagonoffmeshconnections(offmeshconnectionindices:flag:).md)
  Removes the flag from the off-mesh connections at these indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/removeflagonpolygons(polygonindices:flag:))*