# uiTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An optional texture containing your game’s custom UI that this frame interpolator evaluates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var uiTexture: (any MTLTexture)? { get set }
```

#### Discussion

The frame interpolator uses this property to overlay your custom UI on any frame data it produces into [`outputTexture`](mtlfxframeinterpolatorbase/outputtexture.md).

Use property [`isUITextureComposited`](mtlfxframeinterpolatorbase/isuitexturecomposited.md) to indicate to this frame interpolator if [`colorTexture`](mtlfxframeinterpolatorbase/colortexture.md) contains a precomposition of this UI to avoid it producing incorrect results for the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/uitexture)*