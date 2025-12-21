# isUITextureComposited

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A Boolean value that controls whether this frame interpolator interprets the color texture to include your game’s custom UI.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isUITextureComposited: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) when property [`uiTexture`](mtlfxframeinterpolatorbase/uitexture.md) contains a precomposition of any custom UI image on top of the color image.

When you enable this property, the frame interpolator decomposites the color image [`colorTexture`](mtlfxframeinterpolatorbase/colortexture.md) references from the UI [`uiTexture`](mtlfxframeinterpolatorbase/uitexture.md) references before compositing the UI on to the [`outputTexture`](mtlfxframeinterpolatorbase/outputtexture.md).

This property’s default value is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/isuitexturecomposited)*