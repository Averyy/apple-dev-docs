# geometryWithMDLMesh:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a geometry from the specified Model I/O mesh object.

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
+ (instancetype) geometryWithMDLMesh:(MDLMesh *) mdlMesh;
```

## Return Value

A new geometry object.

## Discussion

The Model I/O framework provides universal support for import, export, description, and processing of several 3D asset file formats and related resources. (For details, see [Model I/O](../../ModelIO/ModelIO.md).) The [`MDLMesh`](../../ModelIO/mdlmesh.md) class is a generic description of a 3D object, with vertex buffers corresponding to SceneKit geometry sources, and submeshes corresponding to SceneKit geometry elements. Because Model I/O associates materials with a mesh through its submeshes, importing a [`MDLMesh`](../../ModelIO/mdlmesh.md) object imports the materials assigned to its submeshes to the corresponding locations in the SceneKit geometry’s [`materials`](./materials.md) array.

## Parameters

- `mdlMesh`: A Model I/O mesh object.

## See Also

### Creating a Geometry Object
- [convenience init(sources: [SCNGeometrySource], elements: [SCNGeometryElement]?)](./init%28sources,elements%29.md)
  Creates a new geometry built from the specified geometry sources and elements.
- [+ geometry](./geometry.md)
  Creates a new geometry object with no content (or default content).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/geometrywithmdlmesh:)*