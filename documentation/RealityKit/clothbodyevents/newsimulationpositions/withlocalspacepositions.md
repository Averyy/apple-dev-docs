# withLocalSpacePositions(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the new simulation positions of the body’s particles, in local space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withLocalSpacePositions<Result>(_ body: (Span<SIMD3<Float>>) -> Result) -> Result
```

#### Return Value

The value returned by `body`.

#### Discussion

The provided span is only valid for the lifetime of the callback.

## Parameters

- `body`: A closure that receives a span over the local-space particle positions.

## See Also

- [var localSpacePositions: Span<SIMD3<Float>>](clothbodyevents/newsimulationpositions/localspacepositions.md)
  The new simulation positions of the body’s particles, in local space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodyevents/newsimulationpositions/withlocalspacepositions(_:))*