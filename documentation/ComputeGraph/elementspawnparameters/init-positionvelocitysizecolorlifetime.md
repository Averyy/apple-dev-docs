# init(position:velocity:size:color:lifetime:)

**Framework**: Compute Graph  
**Kind**: init

Creates a new set of particle spawn parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
init(position: SIMD3<Float>, velocity: SIMD3<Float> = .zero, size: SIMD2<Float> = .init(0.01, 0.01), color: SIMD4<Float> = .init(1, 1, 1, 1), lifetime: Float = 1.0)
```

#### Example

```swift
// Create a particle that starts at the origin, moves upward, is red, and lasts 3 seconds
let params = ElementSpawnParameters(
    position: SIMD3<Float>(0, 0, 0),
    velocity: SIMD3<Float>(0, 2, 0),
    size: SIMD2<Float>(0.05, 0.05),
    color: SIMD4<Float>(1, 0, 0, 1),
    lifetime: 3.0
)
```

## Parameters

- `position`: The initial 3D position in world space coordinates
- `velocity`: The initial velocity vector in world space units per second (defaults to zero)
- `size`: The initial size as width and height in world space units (defaults to 0.01 x 0.01)
- `color`: The initial RGBA color (defaults to opaque white)
- `lifetime`: The particle lifetime in seconds (defaults to 1.0 second)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/init(position:velocity:size:color:lifetime:))*