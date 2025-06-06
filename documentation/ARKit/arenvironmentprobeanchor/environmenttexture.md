# environmentTexture

**Framework**: ARKit  
**Kind**: property

A cube-map texture that represents the view in all directions from the probe anchor’s position.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var environmentTexture: (any MTLTexture)? { get }
```

#### Discussion

This texture is in the format [`MTLPixelFormat.bgra8Unorm_srgb`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/bgra8Unorm_srgb).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor/environmenttexture)*