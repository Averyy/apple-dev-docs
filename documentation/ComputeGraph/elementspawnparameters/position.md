# position

**Framework**: Compute Graph  
**Kind**: property

The initial 3D position of the particle in world space coordinates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
var position: SIMD3<Float> { get set }
```

#### Discussion

This determines where the particle will first appear when spawned. The coordinate system follows RealityKit’s conventions with Y pointing up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/position)*