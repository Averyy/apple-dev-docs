# geometryElementWithMDLSubmesh:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a geometry element from the specified Model I/O submesh object.

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
+ (instancetype) geometryElementWithMDLSubmesh:(MDLSubmesh *) mdlSubMesh;
```

#### Return Value

A new geometry element.

#### Discussion

The Model I/O framework provides universal support for import, export, description, and processing of several 3D asset file formats and related resources. (For details, see [Model I/O](../../ModelIO/ModelIO.md).) The [`MDLSubmesh`](../../ModelIO/mdlsubmesh.md) class is a generic description of an index buffer to be used in rendering a 3D object, along with an assigned material.

In SceneKit, materials are assigned to a geometry rather than to its elements, so importing a submesh as a geometry element does not import its material assignment. To import a Model I/O mesh along with its materials, use the [`SCNGeometry`](../scngeometry.md) [`geometryWithMDLMesh:`](../scngeometry/geometrywithmdlmesh_.md) method.

## Parameters

- `mdlSubMesh`: A Model I/O submesh object.

## See Also

### Creating a Geometry Element
- [convenience init(data: Data?, primitiveType: SCNGeometryPrimitiveType, primitiveCount: Int, bytesPerIndex: Int)](./init%28data,primitivetype,primitivecount,bytesperindex%29.md)
  Creates a geometry element from the specified data and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/geometryelementwithmdlsubmesh:)*