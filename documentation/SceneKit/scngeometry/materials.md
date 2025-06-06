# materials

**Framework**: SceneKit  
**Kind**: property

An array of [`SCNMaterial`](scnmaterial.md) objects that determine the geometry’s appearance when rendered.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var materials: [SCNMaterial] { get set }
```

#### Discussion

Materials provide the information SceneKit uses to add color, lighting, texture, and special effects when rendering a geometry. Each [`SCNMaterial`](scnmaterial.md) object can be shared between several geometries.

If a geometry contains multiple elements (see [`elementCount`](scngeometry/elementcount.md)), you can associate a separate material with each geometry element. For example, the teapot in [`Figure 1`](scngeometry/1523472-materials#1965912.md) has four elements, each with a different material.

![None](https://docs-assets.developer.apple.com/published/383165faecb34123302d3458e9a6f41e/media-1965912%402x.png)

If a geometry has the same number of materials as it has geometry elements, the material index corresponds to the element index. For geometries with fewer materials than elements, SceneKit determines the material index for each element by calculating the index of that element modulo the number of materials. For example, in a geometry with six elements and three materials, SceneKit renders the element at index `5` using the material at index `5 % 3 = 2`.

## See Also

- [var firstMaterial: SCNMaterial?](scngeometry/firstmaterial.md)
  The first material attached to the geometry.
- [func material(named: String) -> SCNMaterial?](scngeometry/material(named:).md)
  Returns the first material attached to the geometry with the specified name.
- [func insertMaterial(SCNMaterial, at: Int)](scngeometry/insertmaterial(_:at:).md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](scngeometry/removematerial(at:).md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](scngeometry/replacematerial(at:with:).md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/materials)*