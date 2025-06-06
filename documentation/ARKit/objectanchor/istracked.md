# isTracked

**Framework**: ARKit  
**Kind**: property

A Boolean value that indicates whether the framework is currently tracking an object anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var isTracked: Bool { get }
```

## See Also

- [var boundingBox: ObjectAnchor.AxisAlignedBoundingBox](objectanchor/boundingbox.md)
  The bounding box of an anchor.
- [ObjectAnchor.AxisAlignedBoundingBox](objectanchor/axisalignedboundingbox.md)
  Values that describe an axis-aligned bounding box.
- [var description: String](objectanchor/description.md)
  A textual representation of this anchor.
- [var originFromAnchorTransform: simd_float4x4](objectanchor/originfromanchortransform.md)
  The transform from the object anchor to the origin coordinate system.
- [var referenceObject: ReferenceObject](objectanchor/referenceobject.md)
  The reference object that an anchor corresponds to.
- [var inputFile: URL?](referenceobject/inputfile.md)
  The input file the framework uses for loading a reference object.
- [var usdzFile: URL?](referenceobject/usdzfile.md)
  The trained USDZ file, if the reference object includes one.
- [struct ReferenceObject](referenceobject.md)
  An object the framework can track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objectanchor/istracked)*