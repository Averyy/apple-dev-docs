# material(named:)

**Framework**: SceneKit  
**Kind**: method

Returns the first material attached to the geometry with the specified name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func material(named name: String) -> SCNMaterial?
```

#### Return Value

A material object with the specified name.

#### Discussion

You can use the [`name`](scnmaterial/name.md) property of each [`SCNMaterial`](scnmaterial.md) object to make managing your scene graph easier. Materials loaded from a scene file may have names assigned by an artist using a 3D authoring tool.

If a geometry has multiple materials attached with the same name, this method returns the first according to the order of the [`materials`](scngeometry/materials.md) array.

## Parameters

- `name`: The name of the material to be retrieved.

## See Also

- [var materials: [SCNMaterial]](scngeometry/materials.md)
  An array of [`SCNMaterial`](scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [var firstMaterial: SCNMaterial?](scngeometry/firstmaterial.md)
  The first material attached to the geometry.
- [func insertMaterial(SCNMaterial, at: Int)](scngeometry/insertmaterial(_:at:).md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](scngeometry/removematerial(at:).md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](scngeometry/replacematerial(at:with:).md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/material(named:))*