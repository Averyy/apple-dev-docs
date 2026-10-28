# uiTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An optional texture containing your game’s custom UI that this frame interpolator evaluates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
var uiTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, setter=setUITexture:, nullable) id<MTLTexture> uiTexture;
```

## Discussion

The frame interpolator uses this property to overlay your custom UI on any frame data it produces into [`outputTexture`](./outputtexture.md).

Use property [`isUITextureComposited`](./isuitexturecomposited.md) to indicate to this frame interpolator if this texture contains a precomposition of [`colorTexture`](./colortexture.md)and UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/uitexture)*