# MTLBlendFactor.source1Color

**Framework**: Metal  
**Kind**: case

Blend factor of source values. This option supports dual-source blending and reads from the second color output of the fragment function.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case source1Color
```

#### Discussion

`F(rgb) = Source.rgb`

`F(a) = Source.a`

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblendfactor/source1color)*