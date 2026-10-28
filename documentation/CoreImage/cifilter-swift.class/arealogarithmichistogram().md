# areaLogarithmicHistogram()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Returns a logarithmic histogram of a specified area of the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram
```

```objc
+ (CIFilter<CIAreaLogarithmicHistogram> *) areaLogarithmicHistogramFilter;
```

## Return Value

A 1-pixel-high image containing the calculated histogram`.`

## Discussion

This filter calculates histograms of the `red,``green,``blue,` and `alpha` colors for the specified area of an image. A base two-logarithm function is applied to the values before binning. The `count` property controls the number of bins (or width) of the histogram. The histogram is scaled so that all the values sum to `scale`.

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) that specifies the subregion of the image you want to process.
- **`scale`**: The scale value for the histogram values. If the scale is `1`, then the bins in the resulting image sum to `1`.
- **`count`**: The number of bins for the histogram. This value determines the width of the output image. Minimum value `1`, and maximum value `2048`.
- **`minimumStop`**: The minimum of the range of color channel values in the logarithmic histogram image. Defaults to `-10`.
- **`maximumStop`**: The maximum of the range of color channel values in the logarithmic histogram image. Defaults to 4.

The following code creates a filter that results in a 1-pixel-tall image with a width of 256. The pixel color components contain the logarithmic histogram values:

```swift
func areaLogarithmicHistogram(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaLogarithmicHistogram()
    filter.inputImage = inputImage
    filter.count = 256
    filter.scale = 15
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

Use the [`histogramDisplay()`](./histogramdisplay%28%29.md) filter to display the histogram:

```swift
func logarithmicHistogramDisplay(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.histogramDisplay()
    filter.inputImage = areaLogarithmicHistogram(inputImage: inputImage)
    filter.highLimit = 1
    filter.height = 100
    filter.lowLimit = 0
    return filter.outputImage!
}
```

![Two images arranged horizontally. The image on the left contains a photograph of a vineyard. The lower third of the image contains gravel with a deep shadow in the foreground. The middle of the image shows the vineyard receding into the distance. The top of the image shows a partially cloudy sky. The image on the right shows the result of the logarithmic histogram display filter. There are three overlayed charts showing the histogram of the red, green and blue components.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407281@2x.png)

## See Also

### Filters
- [class func areaAverage() -> any CIFilter & CIAreaAverage](./areaaverage%28%29.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](./areahistogram%28%29.md)
  Returns a histogram of a specified area of the image.
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
- [class func histogramDisplay() -> any CIFilter & CIHistogramDisplay](./histogramdisplay%28%29.md)
  Generates a histogram map from the image.
- [class func kMeans() -> any CIFilter & CIKMeans](./kmeans%28%29.md)
  Applies the k-means algorithm to find the most common colors in an image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](./rowaverage%28%29.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/arealogarithmichistogram())*