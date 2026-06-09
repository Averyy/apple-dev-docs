# springStiffness

**Framework**: RealityKit  
**Kind**: property

The resistance to compressing and stretching between adjacent particles.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var springStiffness: Float { get set }
```

#### Discussion

The valid range is [0.0, 1.0], both included. Values outside the valid range are clamped. The default value is `1.0`.

## See Also

- [var bendStiffness: Float](clothbodymaterial/bendstiffness.md)
  The resistance to bending between adjacent triangles.
- [var crossTetherStiffness: Float](clothbodymaterial/crosstetherstiffness.md)
  The resistance to shearing between opposing vertices.
- [var laplacianDamping: Float](clothbodymaterial/laplaciandamping.md)
  Damping applied to the velocities of the particles, based on the velocities of their connecting particles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodymaterial/springstiffness)*