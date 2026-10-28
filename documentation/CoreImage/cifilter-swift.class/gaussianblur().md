# gaussianBlur()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Blurs an image with a Gaussian distribution pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func gaussianBlur() -> any CIFilter & CIGaussianBlur
```

```objc
+ (CIFilter<CIGaussianBlur> *) gaussianBlurFilter;
```

## Return Value

The blurred image.

## Discussion

This method applies a Gaussian blur filter to an image. The effect targets the pixels within a circle defined by a `radius` and uses Gaussian ditribution to blur the image from the center out.

The Gaussian blur filter uses the following properties:

- **`radius`**: A `float` representing the area of effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`inputImage`**: A [`CIImage`](../ciimage.md) representing the input image to apply the filter to.

The following code creates a filter that adds a heavy blur to the input image:

```swift
    func gaussianBlur(inputImage: CIImage) -> CIImage? {

        let gaussianBlurFilter = CIFilter.gaussianBlur()
        gaussianBlurFilter.inputImage = inputImage
        gaussianBlurFilter.radius = 10
        return gaussianBlurFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. A Gaussian blur filter has been applied to the photo on the right. It is smaller than the one on the left, and has an intense blur effect that makes the entire image very hazy.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3544963@2x.png)

## See Also

### Filters
- [class func bokehBlur() -> any CIFilter & CIBokehBlur](./bokehblur%28%29.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](./boxblur%28%29.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](./discblur%28%29.md)
  Applies a circle-shaped blur to an area of an image.
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
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](./morphologyrectanglemaximum%28%29.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](./morphologyrectangleminimum%28%29.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](./motionblur%28%29.md)
  Creates motion blur on an image.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](./noisereduction%28%29.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](./zoomblur%28%29.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/gaussianblur())*