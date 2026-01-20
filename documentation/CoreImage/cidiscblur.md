# CIDiscBlur

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a disc blur filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIDiscBlur : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cidiscblur/inputimage.md)
  The image to use as an input image.
- [var radius: Float](cidiscblur/radius.md)
  The radius of the blur, in pixels.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter-swift.class/discblur.md)
  Applies a circle-shaped blur to an area of an image.
- [protocol CIBokehBlur](cibokehblur.md)
  The properties you use to configure a bokeh blur filter.
- [protocol CIBoxBlur](ciboxblur.md)
  The properties you use to configure a box blur filter.
- [protocol CIGaussianBlur](cigaussianblur.md)
  The properties you use to configure a Gaussian blur filter.
- [protocol CIMaskedVariableBlur](cimaskedvariableblur.md)
  The properties you use to configure a masked variable blur filter.
- [protocol CIMedian](cimedian.md)
  The properties you use to configure a median filter.
- [protocol CIMorphologyGradient](cimorphologygradient.md)
  The properties you use to configure a morphology gradient filter.
- [protocol CIMorphologyMaximum](cimorphologymaximum.md)
  The properties you use to configure a morphology maximum filter.
- [protocol CIMorphologyMinimum](cimorphologyminimum.md)
  The properties you use to configure a morphology minimum filter.
- [protocol CIMorphologyRectangleMaximum](cimorphologyrectanglemaximum.md)
  The properties you use to configure a morphology rectangle maximum filter.
- [protocol CIMorphologyRectangleMinimum](cimorphologyrectangleminimum.md)
  The properties you use to configure a morphology rectangle minimum filter.
- [protocol CIMotionBlur](cimotionblur.md)
  The properties you use to configure a motion blur filter.
- [protocol CINoiseReduction](cinoisereduction.md)
  The properties you use to configure a noise reduction filter.
- [protocol CIZoomBlur](cizoomblur.md)
  The properties you use to configure a zoom blur filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidiscblur)*