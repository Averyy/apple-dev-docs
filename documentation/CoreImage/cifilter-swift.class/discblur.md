# discBlur()

**Framework**: Core Image  
**Kind**: method

Applies a circle-shaped blur to an area of an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func discBlur() -> any CIFilter & CIDiscBlur
```

#### Return Value

The blurred image.

#### Discussion

This method applies the disc blur filter to an image. The effect targets the pixels within a circle defined by a `radius` and calculates the median color value to create to the output image.

The disc blur filter uses the following properties:

The following code creates a filter that adds a strong blur to the input image:

```swift
    func discBlur(inputImage: CIImage) -> CIImage? {

        let discBlurFilter = CIFilter.discBlur()
        discBlurFilter.inputImage = inputImage
        discBlurFilter.radius = 8
        return discBlurFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a disc blur filter has been applied that creates a strong blur effect on the palm trees in the foreground of the image.](https://docs-assets.developer.apple.com/published/6e6d6f0dd66aad4f24002217ca3e55da/media-3544964%402x.png)

## See Also

- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter-swift.class/bokehblur.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter-swift.class/boxblur.md)
  Applies a square-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter-swift.class/gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.
- [class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur](cifilter-swift.class/maskedvariableblur.md)
  Blurs a specified portion of an image.
- [class func median() -> any CIFilter & CIMedian](cifilter-swift.class/median.md)
  Calculates the median of an image to refine detail.
- [class func morphologyGradient() -> any CIFilter & CIMorphologyGradient](cifilter-swift.class/morphologygradient.md)
  Detects and highlights edges of objects.
- [class func morphologyMaximum() -> any CIFilter & CIMorphologyMaximum](cifilter-swift.class/morphologymaximum.md)
  Blurs a circular area by enlarging contrasting pixels.
- [class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum](cifilter-swift.class/morphologyminimum.md)
  Blurs a circular area by reducing contrasting pixels.
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](cifilter-swift.class/morphologyrectanglemaximum.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](cifilter-swift.class/morphologyrectangleminimum.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter-swift.class/motionblur.md)
  Creates motion blur on an image.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](cifilter-swift.class/noisereduction.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter-swift.class/zoomblur.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/discblur())*