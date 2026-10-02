# viewToClipMatrix

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The view-to-clip coordinates transformation matrix this frame interpolator uses as part of its operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.1+

## Declaration

```swift
var viewToClipMatrix: simd_float4x4 { get set }
```

#### Discussion

Set this to your unmodified projection matrix. Its depth range has to agree with [`isDepthReversed`](mtlfxframeinterpolatorbase/isdepthreversed.md): when that property is `NO` this matrix maps the near plane to a clip z of 0, and when it is `YES` it maps the near plane to a clip z of 1. Both a left-handed and a right-handed matrix are fine, as long as it is the one that produced [`depthTexture`](mtlfxframeinterpolatorbase/depthtexture.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/viewtoclipmatrix)*