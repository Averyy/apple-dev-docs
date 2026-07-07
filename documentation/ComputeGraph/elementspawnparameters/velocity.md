# velocity

**Framework**: Compute Graph  
**Kind**: property

The initial velocity vector of the particle in world space units per second.

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
var velocity: SIMD3<Float> { get set }
```

#### Discussion

This determines the particle’s initial direction and speed of movement. The magnitude of the vector represents the speed, while the direction represents the movement direction. A zero velocity means the particle starts stationary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/velocity)*