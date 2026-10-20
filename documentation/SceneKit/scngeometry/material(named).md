# material(named:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the first material attached to the geometry with the specified name.

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
func material(named name: String) -> SCNMaterial?
```

```objc
- (SCNMaterial *) materialWithName:(NSString *) name;
```

#### Return Value

A material object with the specified name.

#### Discussion

You can use the [`name`](../scnmaterial/name.md) property of each [`SCNMaterial`](../scnmaterial.md) object to make managing your scene graph easier. Materials loaded from a scene file may have names assigned by an artist using a 3D authoring tool.

If a geometry has multiple materials attached with the same name, this method returns the first according to the order of the [`materials`](./materials.md) array.

## Parameters

- `name`: The name of the material to be retrieved.

## See Also

### Managing a Geometry’s Materials
- [var materials: [SCNMaterial]](./materials.md)
  An array of [`SCNMaterial`](../scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [var firstMaterial: SCNMaterial?](./firstmaterial.md)
  The first material attached to the geometry.
- [func insertMaterial(SCNMaterial, at: Int)](./insertmaterial%28_,at%29.md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](./removematerial%28at%29.md)
  Removes a material attached to the geometry.
- [func replaceMaterial(at: Int, with: SCNMaterial)](./replacematerial%28at,with%29.md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/material(named:))*