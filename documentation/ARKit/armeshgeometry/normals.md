# normals

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Rays that define which direction is outside for each face.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var normals: ARGeometrySource { get }
```

```objc
@property (nonatomic, strong, readonly) ARGeometrySource * normals;
```

## See Also

### Getting Geometry Information
- [var classification: ARGeometrySource?](./classification.md)
  Classification for each face in the mesh.
- [enum ARMeshClassification](../armeshclassification.md)
  Enumeration of different classes of real-world objects that ARKit can identify.
- [var faces: ARGeometryElement](./faces.md)
  An object that contains a buffer of vertex indices of the geometry’s faces.
- [class ARGeometryElement](../argeometryelement.md)
  A container for index data, such as vertex indices of a face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armeshgeometry/normals)*