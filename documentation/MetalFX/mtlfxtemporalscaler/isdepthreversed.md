# isDepthReversed

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var isDepthReversed: Bool { get set }
```

## See Also

- [var depthTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.
- [var depthTexture: (any MTLTexture)?](mtlfxtemporalscaler/depthtexture.md)
  An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/isdepthreversed)*