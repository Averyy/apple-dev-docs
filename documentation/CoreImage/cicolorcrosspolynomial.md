# CIColorCrossPolynomial

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a color cross-polynomial filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIColorCrossPolynomial : CIFilterProtocol
```

## Topics

### Instance Properties
- [var blueCoefficients: CIVector](cicolorcrosspolynomial/bluecoefficients.md)
  Polynomial coefficients for the blue channel.
- [var greenCoefficients: CIVector](cicolorcrosspolynomial/greencoefficients.md)
  Polynomial coefficients for the green channel.
- [var inputImage: CIImage?](cicolorcrosspolynomial/inputimage.md)
  The image to use as an input image.
- [var redCoefficients: CIVector](cicolorcrosspolynomial/redcoefficients.md)
  Polynomial coefficients for the red channel.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter-swift.class/colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [protocol CIColorCube](cicolorcube.md)
  The properties you use to configure a color cube filter.
- [protocol CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md)
  The properties you use to configure a color cube with color space filter.
- [protocol CIColorCubesMixedWithMask](cicolorcubesmixedwithmask.md)
  The properties you use to configure a color cube mixed with mask filter.
- [protocol CIColorCurves](cicolorcurves.md)
  The properties you use to configure a color curves filter.
- [protocol CIColorInvert](cicolorinvert.md)
  The properties you use to configure a color invert filter.
- [protocol CIColorMap](cicolormap.md)
  The properties you use to configure a color map filter.
- [protocol CIColorMonochrome](cicolormonochrome.md)
  The properties you use to configure a color monochrome filter.
- [protocol CIConvertLab](ciconvertlab.md)
- [protocol CIDither](cidither.md)
  The properties you use to configure a dither filter.
- [protocol CIColorPosterize](cicolorposterize.md)
  The properties you use to configure a color posterize filter.
- [protocol CIDocumentEnhancer](cidocumentenhancer.md)
  The properties you use to configure a document enhancer filter.
- [protocol CIFalseColor](cifalsecolor.md)
  The properties you use to configure a false color filter.
- [protocol CILabDeltaE](cilabdeltae.md)
  The properties you use to configure a Lab Delta E filter.
- [protocol CIMaskToAlpha](cimasktoalpha.md)
  The properties you use to configure a mask-to-alpha filter.
- [protocol CIMaximumComponent](cimaximumcomponent.md)
  The properties you use to configure a maximum component filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcrosspolynomial)*