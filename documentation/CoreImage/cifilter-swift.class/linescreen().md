# lineScreen()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a monochrome image with a series of small lines to add detail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func lineScreen() -> any CIFilter & CILineScreen
```

```objc
+ (CIFilter<CILineScreen> *) lineScreenFilter;
```

## Return Value

The modified image.

## Discussion

This method applies a line screen filter to an image. The effect generates a monochrome image containing a series of lines creating detail. The halftone effect is a set of lines, dots, or circles that contain detail. When viewing the image from a distance, the markings blend together, creating the illusion of continuous lines and shapes. Print media commonly uses this effect.

The line screen filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`center`**: A set of coordinates marking the center of the image as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`angle`**: A `float` representing the angle of the pattern as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`width`**: A `float` representing the distance between lines in the pattern as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`sharpness`**: A `float` representing the sharpness of the pattern as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that creates a monochrome image containing small lines of detail on a black background:

```swift
func line(inputImage: CIImage) -> CIImage {
    let lineScreen = CIFilter.lineScreen()
    lineScreen.inputImage = inputImage
    lineScreen.center = CGPoint(x: 2016, y: 1512)
    lineScreen.angle = 1
    lineScreen.width = 35
    lineScreen.sharpness = 0.7
    return lineScreen.outputImage!
}
```

![Two photographs of a wooden barrel of green artichokes. The artichokes are crisp with good lighting. The photo one the left has no modifications to color or detail. In the photo on the right, a line screen filter is applied, resulting in a lighter, monochrome image with an overlay of lines, creating the detail of the image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3595915@2x.png)

## See Also

### Filters
- [class func circularScreen() -> any CIFilter & CICircularScreen](./circularscreen%28%29.md)
  Adds a circular overlay to an image.
- [class func cmykHalftone() -> any CIFilter & CICMYKHalftone](./cmykhalftone%28%29.md)
  Adds a series of colorful dots to an image.
- [class func dotScreen() -> any CIFilter & CIDotScreen](./dotscreen%28%29.md)
  Creates a monochrome image with a series of dots to add detail.
- [class func hatchedScreen() -> any CIFilter & CIHatchedScreen](./hatchedscreen%28%29.md)
  Creates a monochrome image with a series of lines to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/linescreen())*