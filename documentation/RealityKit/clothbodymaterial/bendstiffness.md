# bendStiffness

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The resistance to bending between adjacent triangles.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var bendStiffness: Float { get set }
```

## Discussion

The valid range is [0.0, 1.0], both included. Values outside the valid range are clamped. The default value is `0.0`.

## See Also

### Configuring stiffness and damping
- [var springStiffness: Float](./springstiffness.md)
  The resistance to compressing and stretching between adjacent particles.
- [var crossTetherStiffness: Float](./crosstetherstiffness.md)
  The resistance to shearing between opposing vertices.
- [var laplacianDamping: Float](./laplaciandamping.md)
  Damping applied to the velocities of the particles, based on the velocities of their connecting particles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodymaterial/bendstiffness)*