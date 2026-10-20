# removeMaterial(at:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes a material attached to the geometry.

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
func removeMaterial(at index: Int)
```

```objc
- (void) removeMaterialAtIndex:(NSUInteger) index;
```

## Parameters

- `index`: The index of the attached material to be removed.

  > ❗ **Important**:  Raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if `index` is beyond the bounds of the [`materials`](./materials.md) array.

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
- [func replaceMaterial(at: Int, with: SCNMaterial)](./replacematerial%28at,with%29.md)
  Replaces a material attached to the geometry with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/removematerial(at:))*