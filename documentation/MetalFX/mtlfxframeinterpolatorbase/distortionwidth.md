# distortionWidth

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The width, in pixels, of the content region within the distortion texture to use as input.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var distortionWidth: Int { get set }
```

#### Discussion

When set to zero (the default), the frame interpolator uses [`contentWidth`](mtlfxframeinterpolatorbase/contentwidth.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/distortionwidth)*