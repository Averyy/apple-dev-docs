# referenceImage

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The reference image that this image anchor tracks.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var referenceImage: ReferenceImage { get }
```

## See Also

### Getting image information
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of the image in world space.
- [var estimatedScaleFactor: Float](./estimatedscalefactor.md)
  The estimated scale factor between the tracked image’s physical size and the reference image’s size.
- [var isTracked: Bool](./istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this image.
- [var description: String](./description.md)
  A textual representation of this anchor.
- [var id: UUID](./id.md)
  The unique identifier of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/imageanchor/referenceimage)*