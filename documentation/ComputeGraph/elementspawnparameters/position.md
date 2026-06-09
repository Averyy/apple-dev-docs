# position

**Framework**: ComputeGraph  
**Kind**: property

The initial 3D position of the particle in world space coordinates.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
var position: SIMD3<Float> { get set }
```

#### Discussion

This determines where the particle will first appear when spawned. The coordinate system follows RealityKit’s conventions with Y pointing up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/position)*