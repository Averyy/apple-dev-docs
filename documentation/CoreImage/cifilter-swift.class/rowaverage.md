# rowAverage()

**Framework**: Core Image  
**Kind**: method

Calculates the average color for the specified row of pixels in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func rowAverage() -> any CIFilter & CIRowAverage
```

#### Return Value

#### Discussion

This method applies the row average filter to an image. This effect calculates the average color for a horizontal row over a region defined by `extent`. The height of the extent determines the width of the resulting image. The height is always 1 pixel.

The row average filter uses the following properties:

The following code creates a filter that calculates the row average for the middle section of an image:

```swift
func rowAverage(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.rowAverage()
    filter.inputImage = inputImage
    filter.extent = CGRect(x: inputImage.extent.width/3, y: 0, width: inputImage.extent.width/3, height: inputImage.extent.height)
    return filter.outputImage!
}
```

![Two images arranged horizontally side by side. The left image contains a photograph of a modern brick building. The middle of the image is highlighted by a rectangle. The right image contains the result of the row average filter applied to the highlighted region of the image. The right image has been rotated by 90 degrees and then stretched horizontally to make is easier to see. It contains colors from the highlighted region of the left image.](https://docs-assets.developer.apple.com/published/e9fa07c22b21abe1fc14cd79873df1d6/media-4331788%402x.png)

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
- [class func histogramDisplay() -> any CIFilter & CIHistogramDisplay](cifilter-swift.class/histogramdisplay.md)
  Generates a histogram map from the image.
- [class func kMeans() -> any CIFilter & CIKMeans](cifilter-swift.class/kmeans.md)
  Applies the k-means algorithm to find the most common colors in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/rowaverage())*