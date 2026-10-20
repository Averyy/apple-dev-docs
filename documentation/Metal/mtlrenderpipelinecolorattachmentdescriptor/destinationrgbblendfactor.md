# destinationRGBBlendFactor

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The destination blend factor (DBF) used by the RGB blend operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var destinationRGBBlendFactor: MTLBlendFactor { get set }
```

```objc
@property (nonatomic) MTLBlendFactor destinationRGBBlendFactor;
```

#### Discussion

The default value is [`MTLBlendFactor.zero`](../mtlblendfactor/zero.md).

## See Also

### Configuring blend factors
- [var destinationAlphaBlendFactor: MTLBlendFactor](./destinationalphablendfactor.md)
  The destination blend factor (DBF) used by the alpha blend operation.
- [var sourceAlphaBlendFactor: MTLBlendFactor](./sourcealphablendfactor.md)
  The source blend factor (SBF) used by the alpha blend operation.
- [var sourceRGBBlendFactor: MTLBlendFactor](./sourcergbblendfactor.md)
  The source blend factor (SBF) used by the RGB blend operation.
- [enum MTLBlendFactor](../mtlblendfactor.md)
  The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values (*F(rgb)*) and alpha values (*F(a)*) are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [`setBlendColor(red:green:blue:alpha:)`](../mtlrendercommandencoder/setblendcolor%28red,green,blue,alpha%29.md) method of `MTLRenderCommandEncoder`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor)*