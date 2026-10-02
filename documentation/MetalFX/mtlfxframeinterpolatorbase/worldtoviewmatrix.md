# worldToViewMatrix

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The world-to-view transformation matrix this frame interpolator uses as part of its operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.1+

## Declaration

```swift
var worldToViewMatrix: simd_float4x4 { get set }
```

#### Discussion

Set this and [`viewToClipMatrix`](mtlfxframeinterpolatorbase/viewtoclipmatrix.md) to the matrices you use to render the scene into the color buffer. This frame interpolator derives camera-only motion from the pair, and treats two identity matrices as “not supplied”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/worldtoviewmatrix)*