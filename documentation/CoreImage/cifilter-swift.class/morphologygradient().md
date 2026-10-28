# morphologyGradient()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Detects and highlights edges of objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func morphologyGradient() -> any CIFilter & CIMorphologyGradient
```

```objc
+ (CIFilter<CIMorphologyGradient> *) morphologyGradientFilter;
```

## Return Value

The blurred image.

## Discussion

This method applies the morphology gradient filter to an image. The effect uses the `radius` to compute and highlight edges of items within the image.

The morphology gradient filter uses the following properties:

- **`radius`**: A `float` representing the area of effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`inputImage`**: A [`CIImage`](../ciimage.md) representing the input image to apply the filter to.

The following code creates a filter that adds darkness to the overall image while the edges in the input photo become brighter:

```swift
    func morphologyGradient(inputImage: CIImage) -> CIImage? {

        let morphologyGradientFilter = CIFilter.morphologyGradient()
        morphologyGradientFilter.inputImage = inputImage
        morphologyGradientFilter.radius = 1
        return morphologyGradientFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a morphology gradient filter has been applied, resulting in an overall darker image while brightening the edges of the palm trees.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3544969@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/morphologygradient())*