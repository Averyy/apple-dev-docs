# distortionTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A distortion field texture that the frame interpolator uses to correct barrel distortion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var distortionTexture: (any MTLTexture)? { get set }
```

#### Discussion

Assign a texture containing a distortion field to this property to enable barrel distortion correction during frame interpolation. The distortion field describes how to remap pixels to correct lens distortion artifacts common in VR or wide-angle camera applications.

You are responsible for providing a texture that matches the output dimensions of the frame interpolator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/distortiontexture)*