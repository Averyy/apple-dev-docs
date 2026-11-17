# depthTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var depthTextureUsage: MTLTextureUsage { get }
```

```objc
@property (nonatomic, readonly) MTLTextureUsage depthTextureUsage;
```

## Discussion

The input texture you set to the [`depthTexture`](./depthtexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options in this property.

## See Also

### Configuring the depth input
- [var depthTexture: (any MTLTexture)?](./depthtexture.md)
  An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.
- [var isDepthReversed: Bool](./isdepthreversed.md)
  A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/depthtextureusage)*