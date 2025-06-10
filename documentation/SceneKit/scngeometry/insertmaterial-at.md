# insertMaterial(_:at:)

**Framework**: SceneKit  
**Kind**: method

Attaches a material to the geometry at the specified index.

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
func insertMaterial(_ material: SCNMaterial, at index: Int)
```

## Parameters

- `material`: The material to attach.
- `index`: The location in the geometry’s   array at which to add the new material.

## See Also

- [var materials: [SCNMaterial]](scngeometry/materials.md)
  An array of [`SCNMaterial`](scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [var firstMaterial: SCNMaterial?](scngeometry/firstmaterial.md)
  The first material attached to the geometry.
- [func material(named: String) -> SCNMaterial?](scngeometry/material(named:).md)
  Returns the first material attached to the geometry with the specified name.
- [func removeMaterial(at: Int)](scngeometry/removematerial(at:).md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](scngeometry/replacematerial(at:with:).md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/insertmaterial(_:at:))*