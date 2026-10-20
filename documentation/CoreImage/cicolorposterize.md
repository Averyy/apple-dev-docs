# CIColorPosterize

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure a color posterize filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CIColorPosterize : CIFilterProtocol
```

```objc
@protocol CIColorPosterize <CIFilter>
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](./cicolorposterize/inputimage.md)
  The image to use as an input image.
- [var levels: Float](./cicolorposterize/levels.md)
  The number of brightness levels to use for each color component.

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)

## See Also

### Related Documentation
- [class func colorPosterize() -> any CIFilter & CIColorPosterize](./cifilter-swift.class/colorposterize%28%29.md)
  Flattens an image’s colors.
### Protocols
- [protocol CIColorCrossPolynomial](./cicolorcrosspolynomial.md)
  The properties you use to configure a color cross-polynomial filter.
- [protocol CIColorCube](./cicolorcube.md)
  The properties you use to configure a color cube filter.
- [protocol CIColorCubeWithColorSpace](./cicolorcubewithcolorspace.md)
  The properties you use to configure a color cube with color space filter.
- [protocol CIColorCubesMixedWithMask](./cicolorcubesmixedwithmask.md)
  The properties you use to configure a color cube mixed with mask filter.
- [protocol CIColorCurves](./cicolorcurves.md)
  The properties you use to configure a color curves filter.
- [protocol CIColorInvert](./cicolorinvert.md)
  The properties you use to configure a color invert filter.
- [protocol CIColorMap](./cicolormap.md)
  The properties you use to configure a color map filter.
- [protocol CIColorMonochrome](./cicolormonochrome.md)
  The properties you use to configure a color monochrome filter.
- [protocol CIConvertLab](./ciconvertlab.md)
- [protocol CIDither](./cidither.md)
  The properties you use to configure a dither filter.
- [protocol CIDocumentEnhancer](./cidocumentenhancer.md)
  The properties you use to configure a document enhancer filter.
- [protocol CIFalseColor](./cifalsecolor.md)
  The properties you use to configure a false color filter.
- [protocol CILabDeltaE](./cilabdeltae.md)
  The properties you use to configure a Lab Delta E filter.
- [protocol CIMaskToAlpha](./cimasktoalpha.md)
  The properties you use to configure a mask-to-alpha filter.
- [protocol CIMaximumComponent](./cimaximumcomponent.md)
  The properties you use to configure a maximum component filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorposterize)*