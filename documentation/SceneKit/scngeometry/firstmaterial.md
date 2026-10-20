# firstMaterial

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The first material attached to the geometry.

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
var firstMaterial: SCNMaterial? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNMaterial * firstMaterial;
```

#### Discussion

Calling this convenience method is equivalent to retrieving the first object from the geometry’s [`materials`](./materials.md) array. This property’s value is `nil` if the geometry has no attached materials.

## See Also

### Managing a Geometry’s Materials
- [var materials: [SCNMaterial]](./materials.md)
  An array of [`SCNMaterial`](../scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [func material(named: String) -> SCNMaterial?](./material%28named%29.md)
  Returns the first material attached to the geometry with the specified name.
- [func insertMaterial(SCNMaterial, at: Int)](./insertmaterial%28_,at%29.md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](./removematerial%28at%29.md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](./replacematerial%28at,with%29.md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/firstmaterial)*