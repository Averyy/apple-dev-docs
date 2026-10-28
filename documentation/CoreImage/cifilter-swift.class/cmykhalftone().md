# cmykHalftone()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (CIFilter<CICMYKHalftone> *) CMYKHalftone;
```

## Return Value

The modified image.

## Discussion

This method applies a CMYK halftone filter to an image. The effect generates an image containing a series of dots. The dots contain only cyan, magenta, yellow, and black colors. Halftone effect is a set of lines, dots, or circles that contain detail. When viewing the image from a distance, the markings blend together creating the illusion of continuous lines and shapes. Print media commonly uses this effect.

The CMYK halftone filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`angle`**: A `float` representing the angle of the pattern as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`width`**: A `float` representing the distance between dots in the pattern as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`sharpness`**: A `float` representing the sharpness of the pattern as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`center`**: A set of coordinates marking the center of the image as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`grayComponentReplacement`**: A `float` representing the grey component to be replaced as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`underColorRemoval`**: A `float` representing the under-color removal value as an [`NSNumber`](../../Foundation/nsnumber.md).

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

![Two photographs of a wooden barrel of green artichokes. The artichokes are crisp with good lighting. The photo on the left has no modifications to color or detail. In the photo on the right, an applied halftone filter results in the image becoming darker with an overlay of small dots of color, creating the detail of the image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3595920@2x.png)

## See Also

### Filters
- [class func circularScreen() -> any CIFilter & CICircularScreen](./circularscreen%28%29.md)
  Adds a circular overlay to an image.
- [class func dotScreen() -> any CIFilter & CIDotScreen](./dotscreen%28%29.md)
  Creates a monochrome image with a series of dots to add detail.
- [class func hatchedScreen() -> any CIFilter & CIHatchedScreen](./hatchedscreen%28%29.md)
  Creates a monochrome image with a series of lines to add detail.
- [class func lineScreen() -> any CIFilter & CILineScreen](./linescreen%28%29.md)
  Creates a monochrome image with a series of small lines to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/cmykhalftone())*