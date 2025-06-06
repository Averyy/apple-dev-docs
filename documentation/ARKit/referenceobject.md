# ReferenceObject

**Framework**: ARKit  
**Kind**: struct

An object the framework can track.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct ReferenceObject
```

## Topics

### Creating reference objects
- [init(from: URL) async throws](referenceobject/init(from:).md)
  Creates a reference object from a URL you provide.
- [init(named: String, from: Bundle?) async throws](referenceobject/init(named:from:).md)
  Creates a reference object from a bundle.
### Inspecting a reference object
- [var id: UUID](referenceobject/id-swift.property.md)
  The unique identifier of this anchor.
- [ReferenceObject.ID](referenceobject/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [var inputFile: URL?](referenceobject/inputfile.md)
  The input file the framework uses for loading a reference object.
- [var usdzFile: URL?](referenceobject/usdzfile.md)
  The trained USDZ file, if the reference object includes one.
- [var name: String](referenceobject/name.md)
  The name of a reference object.
- [var description: String](referenceobject/description.md)
  A textual representation of this reference object.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceobject)*