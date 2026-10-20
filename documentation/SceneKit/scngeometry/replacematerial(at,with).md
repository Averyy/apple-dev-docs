# replaceMaterial(at:with:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Replaces a material attached to the geometry with another.

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
func replaceMaterial(at index: Int, with material: SCNMaterial)
```

```objc
- (void) replaceMaterialAtIndex:(NSUInteger) index withMaterial:(SCNMaterial *) material;
```

## Parameters

- `index`: The index of the attached material to be replaced.

  > ❗ **Important**:  Raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if `index` is beyond the bounds of the [`materials`](./materials.md) array.
- `material`: The material with which to replace the attached material.

## See Also

### Managing a Geometry’s Materials
- [var materials: [SCNMaterial]](./materials.md)
  An array of [`SCNMaterial`](../scnmaterial.md) objects that determine the geometry’s appearance when rendered.
- [var firstMaterial: SCNMaterial?](./firstmaterial.md)
  The first material attached to the geometry.
- [func material(named: String) -> SCNMaterial?](./material%28named%29.md)
  Returns the first material attached to the geometry with the specified name.
- [func insertMaterial(SCNMaterial, at: Int)](./insertmaterial%28_,at%29.md)
  Attaches a material to the geometry at the specified index.
- [func removeMaterial(at: Int)](./removematerial%28at%29.md)
  Removes a material attached to the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/replacematerial(at:with:))*