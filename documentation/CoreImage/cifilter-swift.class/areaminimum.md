# areaMinimum()

**Framework**: Core Image  
**Kind**: method

Calculates the minimum color component values for a specified area of the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func areaMinimum() -> any CIFilter & CIAreaMinimum
```

#### Return Value

A 1 x 1 size image containing the minimum color component values.

#### Discussion

This filter returns the minimum color components in the region defined by `extent`.

The area minimum filter uses the following properties:

The following code creates a filter that calculates the minimum color components of a 500 x 500 set of pixels from the center of the image:

```swift
func areaMinimum(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.areaMinimum()
    filter.inputImage = inputImage
    filter.extent = CGRect(
        x: inputImage.extent.width/2-250,
        y: inputImage.extent.height/2-250,
        width: 500,
        height: 500)
    return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with leaves in the background. A 500 x 500 pixel square in the center of the image is highlighted using an outlined box. The image on the right shows the result of applying the area minimum filter to the 500 x 500 pixel square. The result is a 1 x 1 pixel image containing a color made up of the minimum color components from the square.](https://docs-assets.developer.apple.com/published/b682127ea75207a119a0f6bf6d9e0cd4/media-4331785%402x.png)

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
- [class func rowAverage() -> any CIFilter & CIRowAverage](cifilter-swift.class/rowaverage.md)
  Calculates the average color for the specified row of pixels in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/areaminimum())*