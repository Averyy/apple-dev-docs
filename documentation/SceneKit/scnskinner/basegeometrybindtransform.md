# baseGeometryBindTransform

**Framework**: SceneKit  
**Kind**: property

The coordinate transformation for the skinner’s geometry in its default state.

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
var baseGeometryBindTransform: SCNMatrix4 { get set }
```

#### Discussion

This transformation matrix converts from the geometry’s model coordinate space to that used by the animation skeleton. It should match the coordinate space in which the skeleton (the nodes in the [`bones`](scnskinner/bones.md) array) is initially defined, binding the model to its default pose.

The default value is [`SCNMatrix4Identity`](scnmatrix4identity.md).

## See Also

- [var baseGeometry: SCNGeometry?](scnskinner/basegeometry.md)
  The geometry whose surface the skinner’s animation skeleton deforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/basegeometrybindtransform)*