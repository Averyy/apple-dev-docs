# ObjectAnchor.AxisAlignedBoundingBox

**Framework**: ARKit  
**Kind**: struct

Values that describe an axis-aligned bounding box.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct AxisAlignedBoundingBox
```

## Topics

### Inspecting the bounding box
- [var center: SIMD3<Float>](objectanchor/axisalignedboundingbox/center.md)
  The center of the bounding box.
- [var extent: SIMD3<Float>](objectanchor/axisalignedboundingbox/extent.md)
  The extent of the bounding box.
- [var max: SIMD3<Float>](objectanchor/axisalignedboundingbox/max.md)
  The maximum coordinates for the bounding box.
- [var min: SIMD3<Float>](objectanchor/axisalignedboundingbox/min.md)
  Minimum coordinates for the bounding box.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var boundingBox: ObjectAnchor.AxisAlignedBoundingBox](objectanchor/boundingbox.md)
  The bounding box of an anchor.
- [var description: String](objectanchor/description.md)
  A textual representation of this anchor.
- [var isTracked: Bool](objectanchor/istracked.md)
  A Boolean value that indicates whether the framework is currently tracking an object anchor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objectanchor/axisalignedboundingbox)*