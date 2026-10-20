# isUITextureComposited

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that controls whether this frame interpolator interprets the color texture to include your game’s custom UI.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
var isUITextureComposited: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isUITextureComposited, setter=setIsUITextureComposited:) BOOL uiTextureComposited;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) when property [`uiTexture`](./uitexture.md) contains a precomposition of any custom UI image on top of the color image.

When you enable this property, the frame interpolator decomposites the color image [`colorTexture`](./colortexture.md) references from the UI [`uiTexture`](./uitexture.md) references before compositing the UI on to the [`outputTexture`](./outputtexture.md).

This property’s default value is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/isuitexturecomposited)*