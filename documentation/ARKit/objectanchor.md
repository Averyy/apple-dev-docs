# ObjectAnchor

**Framework**: ARKit  
**Kind**: struct

A reference object ARKit is tracking.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct ObjectAnchor
```

#### Overview

You use object anchors to learn about the position and orientation of a real-world object.

## Topics

### Inspecting an object anchor
- [var boundingBox: ObjectAnchor.AxisAlignedBoundingBox](objectanchor/boundingbox.md)
  The bounding box of an anchor.
- [ObjectAnchor.AxisAlignedBoundingBox](objectanchor/axisalignedboundingbox.md)
  Values that describe an axis-aligned bounding box.
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
### Inspecting and comparing anchors
- [var id: UUID](objectanchor/id-swift.property.md)
  The unique identifier of this anchor.
- [ObjectAnchor.ID](objectanchor/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TrackableAnchor](trackableanchor.md)

## See Also

- [class ObjectTrackingProvider](objecttrackingprovider.md)
  A source of real-time position of reference objects in a person’s environment.
- [Exploring object tracking with ARKit](../visionOS/exploring_object_tracking_with_arkit.md)
  Find and track real-world objects in visionOS using reference objects trained with Create ML.
- [Implementing object tracking in your visionOS app](../visionOS/implementing-object-tracking-in-your-visionOS-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objectanchor)*