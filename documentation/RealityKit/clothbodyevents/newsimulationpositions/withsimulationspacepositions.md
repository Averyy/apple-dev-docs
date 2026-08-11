# withSimulationSpacePositions(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the new simulation positions of the body’s particles, in simulation space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withSimulationSpacePositions<Result>(_ body: (Span<SIMD3<Float>>) -> Result) -> Result
```

#### Return Value

The value returned by `body`.

#### Discussion

The provided span is only valid for the lifetime of the callback.

## Parameters

- `body`: A closure that receives a span over the simulation-space particle positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodyevents/newsimulationpositions/withsimulationspacepositions(_:))*