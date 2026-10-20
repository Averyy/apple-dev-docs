# originFromAnchorTransform

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The location and orientation of a plane in world space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var originFromAnchorTransform: simd_float4x4 { get }
```

## See Also

### Inspecting a plane anchor
- [var alignment: PlaneAnchor.Alignment](./alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [PlaneAnchor.Alignment](./alignment-swift.enum.md)
  Values describing possible general orientations of a detected plane with respect to gravity.
- [var classification: PlaneAnchor.Classification](./classification-swift.property.md)
  Get the classification of this plane.
- [PlaneAnchor.Classification](./classification-swift.enum.md)
  The kinds of object classification a plane anchor can have.
- [var description: String](./description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/originfromanchortransform)*