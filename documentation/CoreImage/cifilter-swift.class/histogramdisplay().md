# histogramDisplay()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a histogram map from the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func histogramDisplay() -> any CIFilter & CIHistogramDisplay
```

```objc
+ (CIFilter<CIHistogramDisplay> *) histogramDisplayFilter;
```

## Return Value

The generated image.

## Discussion

This method applies the histogram display filter to the result of the output from the [`areaHistogram()`](./areahistogram%28%29.md) filter. This effect shows a graphical representation of the tonal distribution of colors in the image.

The histogram display filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md). Typically this is the output from the area histogram filter.
- **`height`**: A `float` representing the height of the generated histogram image as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`lowLimit`**: A `float` representing the fraction of the left portion of the histogram image to make darker as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`hightLimit`**: A `float` representing the fraction of the right portion of the histogram to make lighter as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that results in a histogram diagram generated from the input image:

```swift
func areaHistogram(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaHistogram()
    filter.inputImage = inputImage
    filter.count = 256
    filter.scale = 50
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}

func histogramDisplay(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.histogramDisplay()
    filter.inputImage = areaHistogram(inputImage: inputImage)
    filter.highLimit = 1
    filter.height = 100
    filter.lowLimit = 0
    return filter.outputImage!
}
```

![Two images side by side horizontally. The left image is a modern building with white concrete and tinted glass windows with a clear sky in the background. The right image is the result of applying the histogram display filter to the output of the area histogram filter. There are three overlaid charts representing the histograms for the red, green, and blue components.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4332168@2x.png)

## See Also

### Filters
- [class func areaAverage() -> any CIFilter & CIAreaAverage](./areaaverage%28%29.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](./areahistogram%28%29.md)
  Returns a histogram of a specified area of the image.
- [class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram](./arealogarithmichistogram%28%29.md)
  Returns a logarithmic histogram of a specified area of the image.
- [class func areaMaximum() -> any CIFilter & CIAreaMaximum](./areamaximum%28%29.md)
  Calculates the maximum color components of a specified area of the image.
- [class func areaMaximumAlpha() -> any CIFilter & CIAreaMaximumAlpha](./areamaximumalpha%28%29.md)
  Finds the pixel with the highest alpha value.
- [class func areaMinimum() -> any CIFilter & CIAreaMinimum](./areaminimum%28%29.md)
  Calculates the minimum color component values for a specified area of the image.
- [class func areaMinimumAlpha() -> any CIFilter & CIAreaMinimumAlpha](./areaminimumalpha%28%29.md)
  Calculates the pixel within a specified area that has the smallest alpha value.
- [class func areaMinMax() -> any CIFilter & CIAreaMinMax](./areaminmax%28%29.md)
  Calculates minimum and maximum color components for a specified area of the image.
- [class func areaMinMaxRed() -> any CIFilter & CIAreaMinMaxRed](./areaminmaxred%28%29.md)
  Calculates the minimum and maximum red component value.
- [class func columnAverage() -> any CIFilter & CIColumnAverage](./columnaverage%28%29.md)
  Calculates the average color for a specified column of an image.
- [class func kMeans() -> any CIFilter & CIKMeans](./kmeans%28%29.md)
  Applies the k-means algorithm to find the most common colors in an image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](./rowaverage%28%29.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/histogramdisplay())*