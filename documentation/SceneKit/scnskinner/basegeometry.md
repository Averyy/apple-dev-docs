# baseGeometry

**Framework**: SceneKit  
**Kind**: property

The geometry whose surface the skinner’s animation skeleton deforms.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var baseGeometry: SCNGeometry? { get set }
```

#### Discussion

Use this property to:

- Change the appearance of a skinned model using the geometry’s materials.
- Replace the skinner’s geometry with a different model. The new model must be compatible with the skinner’s animation skeleton (that is, it must have the same number of vertices).

Because multiple skinner objects can reference the same geometry, you can use the geometry with several nodes in your scene, each with a different skinner object to pose the model in different ways.

## See Also

- [var baseGeometryBindTransform: SCNMatrix4](scnskinner/basegeometrybindtransform.md)
  The coordinate transformation for the skinner’s geometry in its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnskinner/basegeometry)*