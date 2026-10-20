# CIXRay

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The properties you use to configure an X-ray filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol CIXRay : CIFilterProtocol
```

```objc
@protocol CIXRay <CIFilter>
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](./cixray/inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](./cifilterprotocol.md)

## See Also

### Related Documentation
- [class func xRay() -> any CIFilter & CIXRay](./cifilter-swift.class/xray%28%29.md)
  Alters an image to make it look like an X-ray image.
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
- [protocol CIColorPosterize](./cicolorposterize.md)
  The properties you use to configure a color posterize filter.
- [protocol CIDocumentEnhancer](./cidocumentenhancer.md)
  The properties you use to configure a document enhancer filter.
- [protocol CIFalseColor](./cifalsecolor.md)
  The properties you use to configure a false color filter.
- [protocol CILabDeltaE](./cilabdeltae.md)
  The properties you use to configure a Lab Delta E filter.
- [protocol CIMaskToAlpha](./cimasktoalpha.md)
  The properties you use to configure a mask-to-alpha filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cixray)*