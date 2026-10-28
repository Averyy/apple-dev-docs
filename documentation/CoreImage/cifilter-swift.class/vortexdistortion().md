# vortexDistortion()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Distorts an image by using a vortex effect created by rotating pixels around a point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func vortexDistortion() -> any CIFilter & CIVortexDistortion
```

```objc
+ (CIFilter<CIVortexDistortion> *) vortexDistortionFilter;
```

## Return Value

The distorted image.

## Discussion

This method applies the vortex distortion filter to an image. This effect distorts an image by rotating pixels around the defined center to simulate a vortex. You can specify the number of rotations to control the strength of the effect.

The vortex distortion filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`angle`**: A `float` representing the angle of the vortex, in radians, as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`center`**: A set of coordinates marking the center of the image as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`radius`**: A `float` representing the amount of pixels the filter uses to create the distortion as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that results in a small vortex effect:

```swift
func vortexDistort(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.vortexDistortion()
    filter.inputImage = inputImage
    filter.radius = 700
    filter.angle = 56.54866776461628
    filter.center = CGPoint(x: 1124, y: 778)
    return filter.outputImage!
}
```

![Two images next to each other. The image on the left contains a black-and-white checkerboard pattern. The image on the right has the vortex distortion filter applied. The center of the image appears to be tightly twisted with the amount of twist decreasing very quickly towards the edge of the image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407301@2x.png)

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
- [class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion](./toruslensdistortion%28%29.md)
  Creates a torus-shaped lens to distort the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/vortexdistortion())*