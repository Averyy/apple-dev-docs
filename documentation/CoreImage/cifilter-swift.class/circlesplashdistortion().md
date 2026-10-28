# circleSplashDistortion()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Distorts an image with radiating circles to the periphery of the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion
```

```objc
+ (CIFilter<CICircleSplashDistortion> *) circleSplashDistortionFilter;
```

## Return Value

The distorted image.

## Discussion

This method applies the circle splash distortion filter to an image. This effect distorts the pixels starting at the circumference of a circle and emanating outward.

The circle splash distortion filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`radius`**: A `float` representing the amount in pixels the filter uses to create the distortion as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`center`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the center of the image.

The following code creates a filter that results in a ripple effect applied to the image:

```swift
func circularSplash(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.circleSplashDistortion()
    filter.inputImage = inputImage
    filter.center = CGPoint(x: 50.0, y: 50.0)
    filter.radius = 2.0
    return filter.outputImage!
}
```

![On the left, an image with a checkerboard pattern. On the right, the same image but with a circle splash distortion applied. The center of the image contains a checkerboard pattern with larger squares than the original. This is surrounded by stretched black and white stripes radiating out to the edge of the image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407306@2x.png)

## See Also

### Filters
- [class func bumpDistortion() -> any CIFilter & CIBumpDistortion](./bumpdistortion%28%29.md)
  Distorts an image with a concave or convex bump.
- [class func bumpDistortionLinear() -> any CIFilter & CIBumpDistortionLinear](./bumpdistortionlinear%28%29.md)
  Linearly distorts an image with a concave or convex bump.
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
- [class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion](./toruslensdistortion%28%29.md)
  Creates a torus-shaped lens to distort the image.
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](./twirldistortion%28%29.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/circlesplashdistortion())*