# firstMaterial

**Framework**: SceneKit  
**Kind**: property

The first material attached to the geometry.

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
var firstMaterial: SCNMaterial? { get set }
```

#### Discussion

Calling this convenience method is equivalent to retrieving the first object from the geometry’s [`materials`](scngeometry/materials.md) array. This property’s value is `nil` if the geometry has no attached materials.

## See Also

- [var materials: [SCNMaterial]](scngeometry/materials.md)
  An array of [`SCNMaterial`](scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [func material(named: String) -> SCNMaterial?](scngeometry/material(named:).md)
  Returns the first material attached to the geometry with the specified name.
- [func insertMaterial(SCNMaterial, at: Int)](scngeometry/insertmaterial(_:at:).md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](scngeometry/removematerial(at:).md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](scngeometry/replacematerial(at:with:).md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/firstmaterial)*