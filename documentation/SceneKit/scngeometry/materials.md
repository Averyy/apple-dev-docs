# materials

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An array of [`SCNMaterial`](../scnmaterial.md) objects that determine the geometry’s appearance when rendered.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var materials: [SCNMaterial] { get set }
```

```objc
@property (nonatomic, copy) NSArray<SCNMaterial *> * materials;
```

## Discussion

Materials provide the information SceneKit uses to add color, lighting, texture, and special effects when rendering a geometry. Each [`SCNMaterial`](../scnmaterial.md) object can be shared between several geometries.

If a geometry contains multiple elements (see [`elementCount`](./elementcount.md)), you can associate a separate material with each geometry element. For example, the teapot in [Figure 1](./api-1523472-materials.md#1965912) has four elements, each with a different material.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-1965912@2x.png)

If a geometry has the same number of materials as it has geometry elements, the material index corresponds to the element index. For geometries with fewer materials than elements, SceneKit determines the material index for each element by calculating the index of that element modulo the number of materials. For example, in a geometry with six elements and three materials, SceneKit renders the element at index `5` using the material at index `5 % 3 = 2`.

## See Also

### Managing a Geometry’s Materials
- [var firstMaterial: SCNMaterial?](./firstmaterial.md)
  The first material attached to the geometry.
- [func material(named: String) -> SCNMaterial?](./material%28named%29.md)
  Returns the first material attached to the geometry with the specified name.
- [func insertMaterial(SCNMaterial, at: Int)](./insertmaterial%28_,at%29.md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](./removematerial%28at%29.md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](./replacematerial%28at,with%29.md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/materials)*