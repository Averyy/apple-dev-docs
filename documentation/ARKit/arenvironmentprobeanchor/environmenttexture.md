# environmentTexture

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A cube-map texture that represents the view in all directions from the probe anchor’s position.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var environmentTexture: (any MTLTexture)? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) id<MTLTexture> environmentTexture;
```

## Discussion

This texture is in the format [`MTLPixelFormat.bgra8Unorm_srgb`](../../Metal/mtlpixelformat/bgra8unorm_srgb.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor/environmenttexture)*