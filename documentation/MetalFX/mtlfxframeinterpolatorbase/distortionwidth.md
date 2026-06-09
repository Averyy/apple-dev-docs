# distortionWidth

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The width, in pixels, of the content region within the distortion texture to use as input.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var distortionWidth: Int { get set }
```

#### Discussion

When set to zero (the default), the frame interpolator uses [`contentWidth`](mtlfxframeinterpolatorbase/contentwidth.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/distortionwidth)*