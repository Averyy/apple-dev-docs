# MTLBlendFactor.oneMinusSource1Alpha

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Blend factor of one minus source alpha. This option supports dual-source blending and reads from the second color output of the fragment function.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case oneMinusSource1Alpha
```

```c
MTLBlendFactorOneMinusSource1Alpha
```

## Discussion

`F = 1 - Source.a`

## See Also

### Blend factors
- [MTLBlendFactor.zero](./zero.md)
  Blend factor of zero.
- [MTLBlendFactor.one](./one.md)
  Blend factor of one.
- [MTLBlendFactor.sourceColor](./sourcecolor.md)
  Blend factor of source values.
- [MTLBlendFactor.oneMinusSourceColor](./oneminussourcecolor.md)
  Blend factor of one minus source values.
- [MTLBlendFactor.sourceAlpha](./sourcealpha.md)
  Blend factor of source alpha.
- [MTLBlendFactor.oneMinusSourceAlpha](./oneminussourcealpha.md)
  Blend factor of one minus source alpha.
- [MTLBlendFactor.destinationColor](./destinationcolor.md)
  Blend factor of destination values.
- [MTLBlendFactor.oneMinusDestinationColor](./oneminusdestinationcolor.md)
  Blend factor of one minus destination values.
- [MTLBlendFactor.destinationAlpha](./destinationalpha.md)
  Blend factor of destination alpha.
- [MTLBlendFactor.oneMinusDestinationAlpha](./oneminusdestinationalpha.md)
  Blend factor of one minus destination alpha.
- [MTLBlendFactor.sourceAlphaSaturated](./sourcealphasaturated.md)
  Blend factor of the minimum of either source alpha or one minus destination alpha.
- [MTLBlendFactor.blendColor](./blendcolor.md)
  A blend factor that applies the blend color’s red, green, and blue components.
- [MTLBlendFactor.oneMinusBlendColor](./oneminusblendcolor.md)
  A blend factor that applies one minus the blend color’s red, green, and blue components.
- [MTLBlendFactor.blendAlpha](./blendalpha.md)
  Blend factor of alpha value.
- [MTLBlendFactor.oneMinusBlendAlpha](./oneminusblendalpha.md)
  Blend factor of one minus alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblendfactor/oneminussource1alpha)*