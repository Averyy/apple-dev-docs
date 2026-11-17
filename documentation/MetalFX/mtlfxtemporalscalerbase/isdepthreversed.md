# isDepthReversed

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the depth texture uses zero to represent the farthest distance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var isDepthReversed: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isDepthReversed) BOOL depthReversed;
```

## See Also

### Configuring the depth input
- [var depthTextureUsage: MTLTextureUsage](./depthtextureusage.md)
  The minimal texture usage options that your app’s input depth texture must set to apply the temporal scaler.
- [var depthTexture: (any MTLTexture)?](./depthtexture.md)
  An input depth texture you set for the temporal scaler that supports the correct depth texture usage options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/isdepthreversed)*