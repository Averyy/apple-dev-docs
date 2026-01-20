# histogramDisplay()

**Framework**: Core Image  
**Kind**: method

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

#### Return Value

The generated image.

#### Discussion

This method applies the histogram display filter to the result of the output from the [`areaHistogram()`](cifilter-swift.class/areahistogram().md) filter. This effect shows a graphical representation of the tonal distribution of colors in the image.

The histogram display filter uses the following properties:

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

![Two images side by side horizontally. The left image is a modern building with white concrete and tinted glass windows with a clear sky in the background. The right image is the result of applying the histogram display filter to the output of the area histogram filter. There are three overlaid charts representing the histograms for the red, green, and blue components.](https://docs-assets.developer.apple.com/published/24a44bbeb4a9e9acd5808409d2244916/media-4332168%402x.png)

## See Also

- [class func areaAverage() -> any CIFilter & CIAreaAverage](cifilter-swift.class/areaaverage.md)
  Returns a 1 x 1 pixel image that contains the average color for the region of interest.
- [class func areaHistogram() -> any CIFilter & CIAreaHistogram](cifilter-swift.class/areahistogram.md)
  Returns a histogram of a specified area of the image.
- [class func areaLogarithmicHistogram() -> any CIFilter & CIAreaLogarithmicHistogram](cifilter-swift.class/arealogarithmichistogram.md)
  Returns a logarithmic histogram of a specified area of the image.
- [class func areaMaximum() -> any CIFilter & CIAreaMaximum](cifilter-swift.class/areamaximum.md)
  Calculates the maximum color components of a specified area of the image.
- [class func areaMaximumAlpha() -> any CIFilter & CIAreaMaximumAlpha](cifilter-swift.class/areamaximumalpha.md)
  Finds the pixel with the highest alpha value.
- [class func areaMinimum() -> any CIFilter & CIAreaMinimum](cifilter-swift.class/areaminimum.md)
  Calculates the minimum color component values for a specified area of the image.
- [class func areaMinimumAlpha() -> any CIFilter & CIAreaMinimumAlpha](cifilter-swift.class/areaminimumalpha.md)
  Calculates the pixel within a specified area that has the smallest alpha value.
- [class func areaMinMax() -> any CIFilter & CIAreaMinMax](cifilter-swift.class/areaminmax.md)
  Calculates minimum and maximum color components for a specified area of the image.
- [class func areaMinMaxRed() -> any CIFilter & CIAreaMinMaxRed](cifilter-swift.class/areaminmaxred.md)
  Calculates the minimum and maximum red component value.
- [class func columnAverage() -> any CIFilter & CIColumnAverage](cifilter-swift.class/columnaverage.md)
  Calculates the average color for a specified column of an image.
- [class func kMeans() -> any CIFilter & CIKMeans](cifilter-swift.class/kmeans.md)
  Applies the k-means algorithm to find the most common colors in an image.
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter-swift.class/rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/histogramdisplay())*