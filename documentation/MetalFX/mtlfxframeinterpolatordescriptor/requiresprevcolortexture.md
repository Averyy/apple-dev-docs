# requiresPrevColorTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the frame interpolator requires the client to provide a previous color texture.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.1+

## Declaration

```swift
var requiresPrevColorTexture: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL requiresPrevColorTexture;
```

#### Discussion

When this property is YES (the default), you must assign a valid texture to the interpolator’s `prevColorTexture` property before encoding. When NO, the frame interpolator internally manages the previous color data and `prevColorTexture` may be nil.

This property’s default value is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/requiresprevcolortexture)*