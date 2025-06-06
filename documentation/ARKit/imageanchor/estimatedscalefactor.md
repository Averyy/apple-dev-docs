# estimatedScaleFactor

**Framework**: ARKit  
**Kind**: property

The estimated scale factor between the tracked image’s physical size and the reference image’s size.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var estimatedScaleFactor: Float { get }
```

#### Discussion

The scale factor is between the tracked image’s size and the [`physicalSize`](referenceimage/physicalsize.md) property on the reference image you supply when you create an image tracking provider. For example, if you supply a reference image and the version that appears in front of someone is three times larger, this property is `3.0`.

## See Also

- [var originFromAnchorTransform: simd_float4x4](imageanchor/originfromanchortransform.md)
  The location and orientation of the image in world space.
- [var referenceImage: ReferenceImage](imageanchor/referenceimage.md)
  The reference image that this image anchor tracks.
- [var isTracked: Bool](imageanchor/istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this image.
- [var description: String](imageanchor/description.md)
  A textual representation of this anchor.
- [var id: UUID](imageanchor/id.md)
  The unique identifier of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/imageanchor/estimatedscalefactor)*