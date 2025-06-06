# depthTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
var depthTexture: (any MTLTexture)? { get set }
```

#### Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`usage`](https://developer.apple.com/documentation/Metal/MTLTexture/usage) property must use the same [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options as (or be a superset of) the temporal scaling effect’s [`depthTextureUsage`](mtlfxtemporalscaler/depthtextureusage.md) property.
- The texture’s dimensions must be equal to the [`inputWidth`](mtlfxtemporalscaler/inputwidth.md) and [`inputHeight`](mtlfxtemporalscaler/inputheight.md) properties.

## See Also

- [var depthTextureUsage: MTLTextureUsage](mtlfxtemporalscaler/depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.
- [var isDepthReversed: Bool](mtlfxtemporalscaler/isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler/depthtexture)*