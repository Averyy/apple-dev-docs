# morphologyRectangleMaximum()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Blurs a rectangular area by enlarging contrasting pixels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum
```

```objc
+ (CIFilter<CIMorphologyRectangleMaximum> *) morphologyRectangleMaximumFilter;
```

## Return Value

The blurred image.

## Discussion

This method applies the morphology rectangle maximum filter to an image. The effect targets a rectangular section of the image, calculating the median color values to find colors that make up more than half the working area. Using this calculation, the effect enlarges the pixels with contrasting colors to take up more of the working area. The effect is then repeated throughout the image.

The morphology rectangle maximum filter uses the following properties:

- **`width`**: A `float` representing the width in pixels of the working area as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`height`**: A `float` representing the height in pixels of the working area as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`inputImage`**: A [`CIImage`](../ciimage.md) representing the input image to apply the filter to.

The following code creates a filter that adds a blur to the input image while brighting the palm trees:

```swift
    func morphologyRectangleMaximum(inputImage: CIImage) -> CIImage? {

        let morphologyRectangleMaximumFilter = CIFilter.morphologyRectangleMaximum()
        morphologyRectangleMaximumFilter.inputImage = inputImage
        morphologyRectangleMaximumFilter.width = 5
        morphologyRectangleMaximumFilter.height = 5
        return morphologyRectangleMaximumFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a morphology rectangle maximum blur has been applied, resulting in the palm trees becoming lighter and less distinct.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3544958@2x.png)

## See Also

### Filters
- [class func bokehBlur() -> any CIFilter & CIBokehBlur](./bokehblur%28%29.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](./boxblur%28%29.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](./discblur%28%29.md)
  Applies a circle-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](./gaussianblur%28%29.md)
  Blurs an image with a Gaussian distribution pattern.
- [class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur](./maskedvariableblur%28%29.md)
  Blurs a specified portion of an image.
- [class func median() -> any CIFilter & CIMedian](./median%28%29.md)
  Calculates the median of an image to refine detail.
- [class func morphologyGradient() -> any CIFilter & CIMorphologyGradient](./morphologygradient%28%29.md)
  Detects and highlights edges of objects.
- [class func morphologyMaximum() -> any CIFilter & CIMorphologyMaximum](./morphologymaximum%28%29.md)
  Blurs a circular area by enlarging contrasting pixels.
- [class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum](./morphologyminimum%28%29.md)
  Blurs a circular area by reducing contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](./morphologyrectangleminimum%28%29.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](./motionblur%28%29.md)
  Creates motion blur on an image.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](./noisereduction%28%29.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](./zoomblur%28%29.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/morphologyrectanglemaximum())*