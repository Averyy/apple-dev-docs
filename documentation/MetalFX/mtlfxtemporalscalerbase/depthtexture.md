# depthTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var depthTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> depthTexture;
```

## Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`usage`](../../Metal/mtltexture/usage.md) property must use the same [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options as (or be a superset of) the temporal scaling effect’s [`depthTextureUsage`](./depthtextureusage.md) property.
- The texture’s dimensions must be equal to the [`inputWidth`](./inputwidth.md) and [`inputHeight`](./inputheight.md) properties.

## See Also

### Configuring the depth input
- [var depthTextureUsage: MTLTextureUsage](./depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.
- [var isDepthReversed: Bool](./isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/depthtexture)*