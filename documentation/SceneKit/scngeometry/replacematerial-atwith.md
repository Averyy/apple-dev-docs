# replaceMaterial(at:with:)

**Framework**: SceneKit  
**Kind**: method

Replaces a material attached to the geometry with another.

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
func replaceMaterial(at index: Int, with material: SCNMaterial)
```

## Parameters

- `index`: The index of the attached material to be replaced.
- `material`: The material with which to replace the attached material.

## See Also

- [var materials: [SCNMaterial]](scngeometry/materials.md)
  An array of [`SCNMaterial`](scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [var firstMaterial: SCNMaterial?](scngeometry/firstmaterial.md)
  The first material attached to the geometry.
- [func material(named: String) -> SCNMaterial?](scngeometry/material(named:).md)
  Returns the first material attached to the geometry with the specified name.
- [func insertMaterial(SCNMaterial, at: Int)](scngeometry/insertmaterial(_:at:).md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](scngeometry/removematerial(at:).md)
  Removes a material attached to the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/replacematerial(at:with:))*