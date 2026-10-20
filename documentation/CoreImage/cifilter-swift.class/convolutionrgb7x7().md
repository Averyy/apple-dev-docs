# convolutionRGB7X7()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Applies a convolution 7 x 7 filter to the RGB components of an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func convolutionRGB7X7() -> any CIFilter & CIConvolution
```

```objc
+ (CIFilter<CIConvolution> *) convolutionRGB7X7Filter;
```

#### Return Value

The convolved image.

#### Discussion

This method applies a 7 x 7 convolution to the `RGB` components image. The effect uses a 7 x 7 area surrounding an input pixel, the pixel itself, and those within a distance of 3 pixels horizontally and vertically. The effect repeats this for every pixel within the image. The work area is then combined with the weight property vector to produce the processed image. This filter differs from the [`convolution7X7()`](./convolution7x7%28%29.md) filter, which processes all of the color components including the alpha component.

The convolution-RGB 7 x 7 filter uses the following properties:

- **`inputImage`**: A [`CIImage`](../ciimage.md) containing the image to process.
- **`weights`**: A [`CIVector`](../civector.md) representing the convolution kernel.
- **`bias`**: A `float` representing the value that’s added to each output pixel.

> **Note**:  When using a nonzero `bias` value, the output image has an infinite extent. You should crop the output image before attempting to render it.

The following code creates a filter that highlights edges in the input image:

```swift
func convolutionRGB7X7(inputImage: CIImage) -> CIImage {
    let convolutionFilter = CIFilter.convolutionRGB7X7()
    convolutionFilter.inputImage = inputImage
    let weights: [CGFloat] = [
        0, 0, -1, -1, -1, 0, 0,
        0, -1, -3, -3, -3, -1, 0,
        -1, -3, 0, 7, 0, -3, -1,
        -1, -3, 7, 25, 7, -3, -1,
        -1, -3, 0, 7, 0, -3, -1,
        0, -1, -3, -3, -3, -1, 0,
        0, 0, -1, -1, -1, 0, 0
    ]
    let kernel = CIVector(values: weights, count: 49)
    convolutionFilter.weights = kernel
    convolutionFilter.bias = 0.0
    return convolutionFilter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photo of the Golden Gate Bridge with a clear sky as the background. The right image shows the result of applying a 7 x 7 convolution kernel that highlights edges. Fine detail and noise in the image are highlighted.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407333@2x.png)

## See Also

### Filters
- [class func convolution3X3() -> any CIFilter & CIConvolution](./convolution3x3%28%29.md)
  Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [class func convolution5X5() -> any CIFilter & CIConvolution](./convolution5x5%28%29.md)
  Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [class func convolution7X7() -> any CIFilter & CIConvolution](./convolution7x7%28%29.md)
  Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [class func convolution9Horizontal() -> any CIFilter & CIConvolution](./convolution9horizontal%28%29.md)
  Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [class func convolution9Vertical() -> any CIFilter & CIConvolution](./convolution9vertical%28%29.md)
  Applies a convolution-9 vertical filter to the `RGBA` components of an image.
- [class func convolutionRGB3X3() -> any CIFilter & CIConvolution](./convolutionrgb3x3%28%29.md)
  Applies a convolution 3 x 3 filter to the `RGB` components of an image.
- [class func convolutionRGB5X5() -> any CIFilter & CIConvolution](./convolutionrgb5x5%28%29.md)
  Applies a convolution 5 x 5 filter to the `RGB` components of an image.
- [class func convolutionRGB9Horizontal() -> any CIFilter & CIConvolution](./convolutionrgb9horizontal%28%29.md)
  Applies a convolution 9 x 1 filter to the RGB components of an image.
- [class func convolutionRGB9Vertical() -> any CIFilter & CIConvolution](./convolutionrgb9vertical%28%29.md)
  Applies a convolution 1 x 9 filter to the RGB components of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/convolutionrgb7x7())*