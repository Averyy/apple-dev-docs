# cmykHalftone()

**Framework**: Core Image  
**Kind**: method

Adds a series of colorful dots to an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func cmykHalftone() -> any CIFilter & CICMYKHalftone
```

#### Return Value

The modified image.

#### Discussion

This method applies a CMYK halftone filter to an image. The effect generates an image containing a series of dots. The dots contain only cyan, magenta, yellow, and black colors. Halftone effect is a set of lines, dots, or circles that contain detail. When viewing the image from a distance, the markings blend together creating the illusion of continuous lines and shapes. Print media commonly uses this effect.

The CMYK halftone filter uses the following properties:

The following code produces an image with visible dots and less color:

```swift
func cmyk(inputImage: CIImage) -> CIImage {
    let cmykHalftone = CIFilter.cmykHalftone()
    cmykHalftone.inputImage = inputImage
    cmykHalftone.angle = 1
    cmykHalftone.width = 35
    cmykHalftone.sharpness = 0.7
    cmykHalftone.center = CGPoint(x: 2016, y: 1512)
    cmykHalftone.grayComponentReplacement = 1
    cmykHalftone.underColorRemoval = 0.1
    return cmykHalftone.outputImage!
}
```

![Two photographs of a wooden barrel of green artichokes. The artichokes are crisp with good lighting. The photo on the left has no modifications to color or detail. In the photo on the right, an applied halftone filter results in the image becoming darker with an overlay of small dots of color, creating the detail of the image.](https://docs-assets.developer.apple.com/published/11ddc00bc9cd17b1fb63d5d03feb95dc/media-3595920%402x.png)

## See Also

- [class func circularScreen() -> any CIFilter & CICircularScreen](cifilter-swift.class/circularscreen.md)
  Adds a circular overlay to an image.
- [class func dotScreen() -> any CIFilter & CIDotScreen](cifilter-swift.class/dotscreen.md)
  Creates a monochrome image with a series of dots to add detail.
- [class func hatchedScreen() -> any CIFilter & CIHatchedScreen](cifilter-swift.class/hatchedscreen.md)
  Creates a monochrome image with a series of lines to add detail.
- [class func lineScreen() -> any CIFilter & CILineScreen](cifilter-swift.class/linescreen.md)
  Creates a monochrome image with a series of small lines to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/cmykhalftone())*