# depthTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var depthTextureUsage: MTLTextureUsage { get }
```

#### Discussion

The input texture you set to the [`depthTexture`](mtlfxtemporalscaler/depthtexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options in this property.

## See Also

- [var depthTexture: (any MTLTexture)?](mtlfxtemporalscaler/depthtexture.md)
  An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.
- [var isDepthReversed: Bool](mtlfxtemporalscaler/isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/depthtextureusage)*