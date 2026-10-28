# areaMaximumAlpha()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Finds the pixel with the highest alpha value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func areaMaximumAlpha() -> any CIFilter & CIAreaMaximumAlpha
```

```objc
+ (CIFilter<CIAreaMaximumAlpha> *) areaMaximumAlphaFilter;
```

## Return Value

A 1 x 1 size image containing the pixel with the maximum alpha value.

## Discussion

This filter returns the pixel with highest alpha value in the region defined by `extent`.

The area maximum alpha filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) that specifies the subregion of the image that you want to process.

The following code creates a filter that results in a single pixel image containing the pixel with the highest alpha value:

```swift
func areaMaximumAlpha(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaMaximumAlpha()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

![Two images side by side arranged horizontally. The left image is a photograph of a modern brick building. A square outline highlights a 500 x 500 pixel region in the image. The right image contains the result of running the area maximum alpha filter. It contains the color with the highest alpha value from the highlighted square.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4332167@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areamaximumalpha())*