# ObjectAnchor.AxisAlignedBoundingBox

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Values that describe an axis-aligned bounding box.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct AxisAlignedBoundingBox
```

## Topics

### Inspecting the bounding box
- [var center: SIMD3<Float>](./axisalignedboundingbox/center.md)
  The center of the bounding box.
- [var extent: SIMD3<Float>](./axisalignedboundingbox/extent.md)
  The extent of the bounding box.
- [var max: SIMD3<Float>](./axisalignedboundingbox/max.md)
  The maximum coordinates for the bounding box.
- [var min: SIMD3<Float>](./axisalignedboundingbox/min.md)
  Minimum coordinates for the bounding box.
### Operators
- [static func == (ObjectAnchor.AxisAlignedBoundingBox, ObjectAnchor.AxisAlignedBoundingBox) -> Bool](./axisalignedboundingbox/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two axis-aligned bounding boxes are equal.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an object anchor
- [var boundingBox: ObjectAnchor.AxisAlignedBoundingBox](./boundingbox.md)
  The bounding box of an anchor.
- [var description: String](./description.md)
  A textual representation of this anchor.
- [var isTracked: Bool](./istracked.md)
  A Boolean value that indicates whether the framework is currently tracking an object anchor.
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The transform from the object anchor to the origin coordinate system.
- [var referenceObject: ReferenceObject](./referenceobject.md)
  The reference object that an anchor corresponds to.
- [var inputFile: URL?](../referenceobject/inputfile.md)
  The input file the framework uses for loading a reference object.
- [var usdzFile: URL?](../referenceobject/usdzfile.md)
  The trained USDZ file, if the reference object includes one.
- [struct ReferenceObject](../referenceobject.md)
  An object the framework can track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objectanchor/axisalignedboundingbox)*