# color

**Framework**: Compute Graph  
**Kind**: property

The initial color and alpha (transparency) of the particle.

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
var color: SIMD4<Float> { get set }
```

#### Discussion

Uses RGBA format where each component ranges from 0.0 to 1.0:

- `x` (red): Red color component
- `y` (green): Green color component
- `z` (blue): Blue color component
- `w` (alpha): Transparency (0.0 = fully transparent, 1.0 = fully opaque)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/color)*