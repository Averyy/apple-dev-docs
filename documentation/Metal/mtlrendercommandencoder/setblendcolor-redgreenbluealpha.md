# setBlendColor(red:green:blue:alpha:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)
```

#### Discussion

The alpha and color values apply to all the render pass’s attachments. The `red`, `green`, and `blue` color parameters apply to the [`MTLBlendFactor.blendColor`](mtlblendfactor/blendcolor.md) and [`MTLBlendFactor.oneMinusBlendColor`](mtlblendfactor/oneminusblendcolor.md) blend factors.

The `alpha` parameter applies to the [`MTLBlendFactor.blendAlpha`](mtlblendfactor/blendalpha.md) and [`MTLBlendFactor.oneMinusBlendAlpha`](mtlblendfactor/oneminusblendalpha.md) blend factors.

The render pipeline’s default blend color value is `0.0` for each parameter, which is equivalent to [`MTLBlendFactor.zero`](mtlblendfactor/zero.md). For other blending factor values, see [`MTLBlendFactor`](mtlblendfactor.md).

## Parameters

- `red`: A value for the red component for the blend color constant.
- `green`: A value for the green component for the blend color constant.
- `blue`: A value for the blue component for the blend color constant.
- `alpha`: A value for the alpha component for the blend color constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:))*