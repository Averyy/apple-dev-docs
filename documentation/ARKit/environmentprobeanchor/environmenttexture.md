# environmentTexture

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The environment texture of an anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var environmentTexture: (any MTLTexture)? { get }
```

## Discussion

The texture stores floating point linear high-dynamic range rgb values in P3 color space.

The texture is `nil` when the person isn’t in a well-lit environment.

## See Also

### Getting anchor information
- [var cameraScaleReference: Float](./camerascalereference.md)
  The camera scale reference of this anchor.
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The transform from the environment probe anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/environmentprobeanchor/environmenttexture)*