# classification

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Get the classification of this plane.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0 (renamed: surfaceClassification)

## Declaration

```swift
var classification: PlaneAnchor.Classification { get }
```

## See Also

### Inspecting a plane anchor
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a plane in world space.
- [var alignment: PlaneAnchor.Alignment](./alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [PlaneAnchor.Alignment](./alignment-swift.enum.md)
  Values describing possible general orientations of a detected plane with respect to gravity.
- [PlaneAnchor.Classification](./classification-swift.enum.md)
  The kinds of object classification a plane anchor can have.
- [var description: String](./description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/classification-swift.property)*