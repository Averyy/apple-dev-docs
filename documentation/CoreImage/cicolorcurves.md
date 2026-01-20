# CIColorCurves

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a color curves filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIColorCurves : CIFilterProtocol
```

## Topics

### Instance Properties
- [var colorSpace: CGColorSpace?](cicolorcurves/colorspace.md)
  The working color space.
- [var curvesData: Data](cicolorcurves/curvesdata.md)
  Color values that determine the color curves transform.
- [var curvesDomain: CIVector](cicolorcurves/curvesdomain.md)
  A two-element vector that defines the minimum and maximum values of the curve data.
- [var inputImage: CIImage?](cicolorcurves/inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorCurves() -> any CIFilter & CIColorCurves](cifilter-swift.class/colorcurves.md)
  Adjusts an image’s color curves.
- [protocol CIColorCrossPolynomial](cicolorcrosspolynomial.md)
  The properties you use to configure a color cross-polynomial filter.
- [protocol CIColorCube](cicolorcube.md)
  The properties you use to configure a color cube filter.
- [protocol CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md)
  The properties you use to configure a color cube with color space filter.
- [protocol CIColorCubesMixedWithMask](cicolorcubesmixedwithmask.md)
  The properties you use to configure a color cube mixed with mask filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcurves)*