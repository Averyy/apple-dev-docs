# convolutionRGB3X3()

**Framework**: Core Image  
**Kind**: method

Applies a convolution 3 x 3 filter to the `RGB` components of an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func convolutionRGB3X3() -> any CIFilter & CIConvolution
```

#### Return Value

The convolved image.

#### Discussion

This method applies a 3 x 3 convolution to the `RGB` components of an image. The effect uses a 3 x 3 area surrounding an input pixel, the pixel itself, and those within a distance of 1 pixel horizontally and vertically. This filter differs from the [`convolution3X3()`](cifilter-swift.class/convolution3x3().md) filter, which processes all of the color components including the alpha component.

The convolution-RGB 3 x 3 filter uses the following properties:

> **Note**:  When using a nonzero `bias` value, the output image has an infinite extent. You should crop the output image before attempting to render it.

The following code creates a filter that sharpens the input image:

```swift
func convolutionRGB3X3(inputImage: CIImage) -> CIImage {
    let convolutionFilter = CIFilter.convolutionRGB3X3()
    convolutionFilter.inputImage = inputImage
    let kernel = CIVector(values: [
        0, -2, 0,
        -2, 9, -2,
        0, -2, 0
    ], count: 9)
    convolutionFilter.weights = kernel
    convolutionFilter.bias = 0.0
    return convolutionFilter.outputImage!
}
```

![Two images arranged horizontally. The left image is of a modern building with horizontal concrete beams and large tinted windows. The right image shows the result of applying the convolution RGB 3 x 3 filter with a kernel that sharpens the image. Edges and fine detail in the image are emphasized.](https://docs-assets.developer.apple.com/published/3822396c355353c595422bd0a53e4d95/media-4407321%402x.png)

## See Also

- [class func convolution3X3() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution3x3.md)
  Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [class func convolution5X5() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution5x5.md)
  Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [class func convolution7X7() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution7x7.md)
  Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [class func convolution9Horizontal() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution9horizontal.md)
  Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [class func convolution9Vertical() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution9vertical.md)
  Applies a convolution-9 vertical filter to the `RGBA` components of an image.
- [class func convolutionRGB5X5() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb5x5.md)
  Applies a convolution 5 x 5 filter to the `RGB` components of an image.
- [class func convolutionRGB7X7() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb7x7.md)
  Applies a convolution 7 x 7 filter to the RGB components of an image.
- [class func convolutionRGB9Horizontal() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb9horizontal.md)
  Applies a convolution 9 x 1 filter to the RGB components of an image.
- [class func convolutionRGB9Vertical() -> any CIFilter & CIConvolution](cifilter-swift.class/convolutionrgb9vertical.md)
  Applies a convolution 1 x 9 filter to the RGB components of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/convolutionrgb3x3())*