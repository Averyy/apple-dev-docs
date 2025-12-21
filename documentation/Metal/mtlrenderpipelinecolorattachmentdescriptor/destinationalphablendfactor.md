# destinationAlphaBlendFactor

**Framework**: Metal  
**Kind**: property

The destination blend factor (DBF) used by the alpha blend operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var destinationAlphaBlendFactor: MTLBlendFactor { get set }
```

#### Discussion

The default value is [`MTLBlendFactor.zero`](mtlblendfactor/zero.md).

## See Also

- [var destinationRGBBlendFactor: MTLBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md)
  The destination blend factor (DBF) used by the RGB blend operation.
- [var sourceAlphaBlendFactor: MTLBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md)
  The source blend factor (SBF) used by the alpha blend operation.
- [var sourceRGBBlendFactor: MTLBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md)
  The source blend factor (SBF) used by the RGB blend operation.
- [enum MTLBlendFactor](mtlblendfactor.md)
  The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values () and alpha values () are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [`setBlendColor(red:green:blue:alpha:)`](mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:).md) method of `MTLRenderCommandEncoder`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor)*