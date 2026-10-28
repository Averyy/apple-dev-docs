# torusLensDistortion()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a torus-shaped lens to distort the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion
```

```objc
+ (CIFilter<CITorusLensDistortion> *) torusLensDistortionFilter;
```

## Return Value

The distorted image.

## Discussion

This method applies the torus lens distortion filter to an image. This effect distorts an image by creating a torus-shaped object, placing it over the input image, and applying the refraction.

The torus lens distortion filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`center`**: A set of coordinates marking the center of the image as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`radius`**: A `float` representing the amount of pixels the filter uses in the tours as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`refraction`**: A `float` representing the refraction of the glass as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`width`**: A `float` representing the width of the torus ring as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that results in a torus-shaped object placed over the image:

```swift
func torusLens(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.torusLensDistortion()
    filter.inputImage = inputImage
    filter.radius = 620
    filter.refraction = 1.7
    filter.center = CGPoint(x: 1791, y: 1344)
    filter.width = 360
    return filter.outputImage!
}
```

![Two images next to each other. The image on the left contains a black-and-white checkerboard pattern. The image on the right has the torus lens distortion filter applied. The image appears to have a ring of distortion around the center.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407288@2x.png)

## See Also

### Filters
- [class func bumpDistortion() -> any CIFilter & CIBumpDistortion](./bumpdistortion%28%29.md)
  Distorts an image with a concave or convex bump.
- [class func bumpDistortionLinear() -> any CIFilter & CIBumpDistortionLinear](./bumpdistortionlinear%28%29.md)
  Linearly distorts an image with a concave or convex bump.
- [class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion](./circlesplashdistortion%28%29.md)
  Distorts an image with radiating circles to the periphery of the image.
- [class func circularWrap() -> any CIFilter & CICircularWrap](./circularwrap%28%29.md)
  Distorts an image by increasing the distance of the center of the image.
- [class func displacementDistortion() -> any CIFilter & CIDisplacementDistortion](./displacementdistortion%28%29.md)
  Applies the grayscale values of the second image to the first image.
- [class func droste() -> any CIFilter & CIDroste](./droste%28%29.md)
  Stylizes an image with the Droste effect.
- [class func glassDistortion() -> any CIFilter & CIGlassDistortion](./glassdistortion%28%29.md)
  Distorts an image by applying a glass-like texture.
- [class func glassLozenge() -> any CIFilter & CIGlassLozenge](./glasslozenge%28%29.md)
  Creates a lozenge-shaped lens and distorts the image.
- [class func holeDistortion() -> any CIFilter & CIHoleDistortion](./holedistortion%28%29.md)
  Distorts an image with a circular area that pushes the image outward.
- [class func lightTunnel() -> any CIFilter & CILightTunnel](./lighttunnel%28%29.md)
  Distorts an image by generating a light tunnel.
- [class func ninePartStretched() -> any CIFilter & CINinePartStretched](./ninepartstretched%28%29.md)
  Distorts an image by stretching it between two breakpoints.
- [class func ninePartTiled() -> any CIFilter & CINinePartTiled](./nineparttiled%28%29.md)
  Distorts an image by tiling portions of it.
- [class func pinchDistortion() -> any CIFilter & CIPinchDistortion](./pinchdistortion%28%29.md)
  Distorts an image by creating a pinch effect with stronger distortion in the center.
- [class func stretchCrop() -> any CIFilter & CIStretchCrop](./stretchcrop%28%29.md)
  Distorts an image by stretching or cropping to fit a specified size.
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](./twirldistortion%28%29.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/toruslensdistortion())*