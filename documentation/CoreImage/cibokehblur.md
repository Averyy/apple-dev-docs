# CIBokehBlur

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a bokeh blur filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIBokehBlur : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cibokehblur/inputimage.md)
  The image to use as an input image.
- [var radius: Float](cibokehblur/radius.md)
  The radius of the blur, in pixels.
- [var ringAmount: Float](cibokehblur/ringamount.md)
  The amount of extra emphasis at the ring of the bokeh.
- [var ringSize: Float](cibokehblur/ringsize.md)
  The radius of the extra emphasis at the ring of the bokeh.
- [var softness: Float](cibokehblur/softness.md)
  The softness of the bokeh effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter-swift.class/bokehblur.md)
  Applies a bokeh effect to an image.
- [protocol CIBoxBlur](ciboxblur.md)
  The properties you use to configure a box blur filter.
- [protocol CIDiscBlur](cidiscblur.md)
  The properties you use to configure a disc blur filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibokehblur)*