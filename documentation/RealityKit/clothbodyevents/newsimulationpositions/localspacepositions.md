# localSpacePositions

**Framework**: RealityKit  
**Kind**: property

The new simulation positions of the body’s particles, in local space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var localSpacePositions: Span<SIMD3<Float>> { get }
```

#### Discussion

The lifetime of this span is tied to the owning event, and thus cannot escape it. This data is only available during the subscription callback in which the owning event is provided. If you store the event and attempt to access this data after the subscription callback, then you will get an empty span instead.

## See Also

- [func withLocalSpacePositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothbodyevents/newsimulationpositions/withlocalspacepositions(_:).md)
  Provides access to the new simulation positions of the body’s particles, in local space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodyevents/newsimulationpositions/localspacepositions)*