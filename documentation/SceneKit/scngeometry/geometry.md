# geometry

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a new geometry object with no content (or default content).

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) geometry;
```

## Return Value

A new geometry object.

## Discussion

This method creates a geometry with no visible content. You can use an empty geometry with another geometry’s [`levelsOfDetail`](./levelsofdetail.md) property to make the geometry disappear when it is too far away from the camera to usefully render.

SceneKit’s [`SCNGeometry`](../scngeometry.md) subclasses use this method to create geometry instances with default contents. For example, if you call this method on the [`SCNSphere`](../scnsphere.md) class, it creates a sphere geometry whose [`radius`](../scnsphere/radius.md) property has the default value of `0.5`.

You cannot add geometry sources or elements to a geometry object after creating it. To create a custom geometry from your own source and element data, use the [`init(sources:elements:)`](./init%28sources,elements%29.md) method.

## See Also

### Creating a Geometry Object
- [convenience init(sources: [SCNGeometrySource], elements: [SCNGeometryElement]?)](./init%28sources,elements%29.md)
  Creates a new geometry built from the specified geometry sources and elements.
- [+ geometryWithMDLMesh:](./geometrywithmdlmesh_.md)
  Creates a geometry from the specified Model I/O mesh object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/geometry)*