# areaAverage()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Returns a 1 x 1 pixel image that contains the average color for the region of interest.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func areaAverage() -> any CIFilter & CIAreaAverage
```

```objc
+ (CIFilter<CIAreaAverage> *) areaAverageFilter;
```

#### Return Value

A 1 x 1 pixel image containing the average color for the region of interest.

#### Discussion

This filter calculates the average color of the area defined by `extent` and creates a 1 x 1 pixel image with the result. The filter processes each color component (red, green, blue, alpha) of the input image independently.

The area average filter uses the following properties:

- **`inputImage`**: The [`CIImage`](../ciimage.md) containing the image you want to process.
- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) that specifies the region of the image that you want to process.

The following code creates a filter that calculates the average color of a 500 x 500 set of pixels from the center of the image:

```swift
func averageArea(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaAverage()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with leaves in the background. A 500 x 500 pixel square in the center of the image is highlighted using a square outline. The image on the right shows the result of applying the area average filter to the 500 x 500 pixel square. The result is a 1 x 1 pixel image containing the average color from the highlighted square of the left image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4331783@2x.png)

## See Also

### Filters
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
- [class func rowAverage() -> any CIFilter & CIRowAverage](./rowaverage%28%29.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areaaverage())*