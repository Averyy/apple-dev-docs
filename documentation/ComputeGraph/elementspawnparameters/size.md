# size

**Framework**: Compute Graph  
**Kind**: property

The initial size of the particle as a 2D vector representing width and height.

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
var size: SIMD2<Float> { get set }
```

#### Discussion

For most particle systems, this represents the billboard size in world space units.

- `x` component: width of the particle
- `y` component: height of the particle

Equal values create square particles, while different values create rectangular particles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/size)*