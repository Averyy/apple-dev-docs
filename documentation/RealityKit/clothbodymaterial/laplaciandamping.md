# laplacianDamping

**Framework**: RealityKit  
**Kind**: property

Damping applied to the velocities of the particles, based on the velocities of their connecting particles.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var laplacianDamping: Float { get set }
```

#### Discussion

Higher values will make the cloth behave more similar to a “wet cloth”.

The valid range is [0.0, 1.0], both included. Values outside the valid range are clamped. The default value is `0.1`.

## See Also

- [var springStiffness: Float](clothbodymaterial/springstiffness.md)
  The resistance to compressing and stretching between adjacent particles.
- [var bendStiffness: Float](clothbodymaterial/bendstiffness.md)
  The resistance to bending between adjacent triangles.
- [var crossTetherStiffness: Float](clothbodymaterial/crosstetherstiffness.md)
  The resistance to shearing between opposing vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodymaterial/laplaciandamping)*