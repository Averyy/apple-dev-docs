# rowAverage()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (CIFilter<CIRowAverage> *) rowAverageFilter;
```

## Return Value

## Discussion

This method applies the row average filter to an image. This effect calculates the average color for a horizontal row over a region defined by `extent`. The height of the extent determines the width of the resulting image. The height is always 1 pixel.

The row average filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) that specifies the subregion of the image that you want to process.

The following code creates a filter that calculates the row average for the middle section of an image:

```swift
func rowAverage(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.rowAverage()
    filter.inputImage = inputImage
    filter.extent = CGRect(x: inputImage.extent.width/3, y: 0, width: inputImage.extent.width/3, height: inputImage.extent.height)
    return filter.outputImage!
}
```

![Two images arranged horizontally side by side. The left image contains a photograph of a modern brick building. The middle of the image is highlighted by a rectangle. The right image contains the result of the row average filter applied to the highlighted region of the image. The right image has been rotated by 90 degrees and then stretched horizontally to make is easier to see. It contains colors from the highlighted region of the left image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4331788@2x.png)

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
- [class func histogramDisplay() -> any CIFilter & CIHistogramDisplay](./histogramdisplay%28%29.md)
  Generates a histogram map from the image.
- [class func kMeans() -> any CIFilter & CIKMeans](./kmeans%28%29.md)
  Applies the k-means algorithm to find the most common colors in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/rowaverage())*