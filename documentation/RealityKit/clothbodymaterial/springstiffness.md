# springStiffness

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The resistance to compressing and stretching between adjacent particles.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var springStiffness: Float { get set }
```

#### Discussion

The valid range is [0.0, 1.0], both included. Values outside the valid range are clamped. The default value is `1.0`.

## See Also

### Configuring stiffness and damping
- [var bendStiffness: Float](./bendstiffness.md)
  The resistance to bending between adjacent triangles.
- [var crossTetherStiffness: Float](./crosstetherstiffness.md)
  The resistance to shearing between opposing vertices.
- [var laplacianDamping: Float](./laplaciandamping.md)
  Damping applied to the velocities of the particles, based on the velocities of their connecting particles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodymaterial/springstiffness)*