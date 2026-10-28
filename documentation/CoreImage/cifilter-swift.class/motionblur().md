# motionBlur()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates motion blur on an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func motionBlur() -> any CIFilter & CIMotionBlur
```

```objc
+ (CIFilter<CIMotionBlur> *) motionBlurFilter;
```

## Return Value

The blurred image.

## Discussion

This method applies the motion blur filter to an image. The filter uses the angle of a single row of pixels to determine the direction of the motion effect.

The motion blur filter uses the following properties:

- **`radius`**: A `float` representing the area of effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`angle`**: A `float` representing the angle of the motion, in radians, that determines which direction the blur smears as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`inputImage`**: A [`CIImage`](../ciimage.md) representing the input image to apply the filter to.

The following code creates a filter that adds a motion blur to the input image:

```swift
    func motionBlur(inputImage: CIImage) -> CIImage? {

        let motionBlurFilter = CIFilter.motionBlur()
        motionBlurFilter.inputImage = inputImage
        motionBlurFilter.angle = 0
        motionBlurFilter.radius = 20
        return motionBlurFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a motion blur filter has been applied, causing a hazy and streaky effect and making the trees in the foreground look very blurry and distorted.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3544965@2x.png)

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
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](./morphologyrectanglemaximum%28%29.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](./morphologyrectangleminimum%28%29.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](./noisereduction%28%29.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](./zoomblur%28%29.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/motionblur())*