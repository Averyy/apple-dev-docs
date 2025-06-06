# MTLBlendFactor

**Framework**: Metal  
**Kind**: enum

The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values () and alpha values () are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [`setBlendColor(red:green:blue:alpha:)`](mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:).md) method of `MTLRenderCommandEncoder`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLBlendFactor
```

## Topics

### Constants
- [MTLBlendFactor.zero](mtlblendfactor/zero.md)
  Blend factor of zero.
- [MTLBlendFactor.one](mtlblendfactor/one.md)
  Blend factor of one.
- [MTLBlendFactor.sourceColor](mtlblendfactor/sourcecolor.md)
  Blend factor of source values.
- [MTLBlendFactor.oneMinusSourceColor](mtlblendfactor/oneminussourcecolor.md)
  Blend factor of one minus source values.
- [MTLBlendFactor.sourceAlpha](mtlblendfactor/sourcealpha.md)
  Blend factor of source alpha.
- [MTLBlendFactor.oneMinusSourceAlpha](mtlblendfactor/oneminussourcealpha.md)
  Blend factor of one minus source alpha.
- [MTLBlendFactor.destinationColor](mtlblendfactor/destinationcolor.md)
  Blend factor of destination values.
- [MTLBlendFactor.oneMinusDestinationColor](mtlblendfactor/oneminusdestinationcolor.md)
  Blend factor of one minus destination values.
- [MTLBlendFactor.destinationAlpha](mtlblendfactor/destinationalpha.md)
  Blend factor of destination alpha.
- [MTLBlendFactor.oneMinusDestinationAlpha](mtlblendfactor/oneminusdestinationalpha.md)
  Blend factor of one minus destination alpha.
- [MTLBlendFactor.sourceAlphaSaturated](mtlblendfactor/sourcealphasaturated.md)
  Blend factor of the minimum of either source alpha or one minus destination alpha.
- [MTLBlendFactor.blendColor](mtlblendfactor/blendcolor.md)
  Blend factor of RGB values.
- [MTLBlendFactor.oneMinusBlendColor](mtlblendfactor/oneminusblendcolor.md)
  Blend factor of one minus RGB values.
- [MTLBlendFactor.blendAlpha](mtlblendfactor/blendalpha.md)
  Blend factor of alpha value.
- [MTLBlendFactor.oneMinusBlendAlpha](mtlblendfactor/oneminusblendalpha.md)
  Blend factor of one minus alpha value.
- [MTLBlendFactor.source1Color](mtlblendfactor/source1color.md)
  Blend factor of source values. This option supports dual-source blending and reads from the second color output of the fragment function.
- [MTLBlendFactor.oneMinusSource1Color](mtlblendfactor/oneminussource1color.md)
  Blend factor of one minus source values. This option supports dual-source blending and reads from the second color output of the fragment function.
- [MTLBlendFactor.source1Alpha](mtlblendfactor/source1alpha.md)
  Blend factor of source alpha. This option supports dual-source blending and reads from the second color output of the fragment function.
- [MTLBlendFactor.oneMinusSource1Alpha](mtlblendfactor/oneminussource1alpha.md)
  Blend factor of one minus source alpha. This option supports dual-source blending and reads from the second color output of the fragment function.
### Initializers
- [init?(rawValue: UInt)](mtlblendfactor/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MTLBlendOperation](mtlblendoperation.md)
  For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.
- [struct MTLColorWriteMask](mtlcolorwritemask.md)
  Values used to specify a mask to permit or restrict writing to color channels of a color value. The values [`red`](mtlcolorwritemask/red.md), [`green`](mtlcolorwritemask/green.md), [`blue`](mtlcolorwritemask/blue.md), and [`alpha`](mtlcolorwritemask/alpha.md) select one color channel each, and they can be bitwise combined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblendfactor)*