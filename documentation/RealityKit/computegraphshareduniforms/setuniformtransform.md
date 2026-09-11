# setUniformTransform(_:)

**Framework**: RealityKit  
**Kind**: method

Registers a closure that transforms a uniform value of type `V` on a per-entity basis.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setUniformTransform<V>(_ transform: @escaping (V, Entity) -> V) where V : BitwiseCopyable
```

#### Discussion

The closure receives the current value and the entity being evaluated, and returns the transformed value. This lets you derive per-entity variants of a global uniform at simulation time, for example, converting a position from the scene’s coordinate system to the system’s coordinate system.

## Parameters

- `transform`: A closure `(V, Entity) -> V`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphshareduniforms/setuniformtransform(_:))*