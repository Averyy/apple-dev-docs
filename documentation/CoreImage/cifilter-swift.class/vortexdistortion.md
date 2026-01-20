# vortexDistortion()

**Framework**: Core Image  
**Kind**: method

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

#### Return Value

The distorted image.

#### Discussion

This method applies the vortex distortion filter to an image. This effect distorts an image by rotating pixels around the defined center to simulate a vortex. You can specify the number of rotations to control the strength of the effect.

The vortex distortion filter uses the following properties:

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

![Two images next to each other. The image on the left contains a black-and-white checkerboard pattern. The image on the right has the vortex distortion filter applied. The center of the image appears to be tightly twisted with the amount of twist decreasing very quickly towards the edge of the image.](https://docs-assets.developer.apple.com/published/932220d9af42464e22c6af5e828fddc4/media-4407301%402x.png)

## See Also

- [class func bumpDistortion() -> any CIFilter & CIBumpDistortion](cifilter-swift.class/bumpdistortion.md)
  Distorts an image with a concave or convex bump.
- [class func bumpDistortionLinear() -> any CIFilter & CIBumpDistortionLinear](cifilter-swift.class/bumpdistortionlinear.md)
  Linearly distorts an image with a concave or convex bump.
- [class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion](cifilter-swift.class/circlesplashdistortion.md)
  Distorts an image with radiating circles to the periphery of the image.
- [class func circularWrap() -> any CIFilter & CICircularWrap](cifilter-swift.class/circularwrap.md)
  Distorts an image by increasing the distance of the center of the image.
- [class func displacementDistortion() -> any CIFilter & CIDisplacementDistortion](cifilter-swift.class/displacementdistortion.md)
  Applies the grayscale values of the second image to the first image.
- [class func droste() -> any CIFilter & CIDroste](cifilter-swift.class/droste.md)
  Stylizes an image with the Droste effect.
- [class func glassDistortion() -> any CIFilter & CIGlassDistortion](cifilter-swift.class/glassdistortion.md)
  Distorts an image by applying a glass-like texture.
- [class func glassLozenge() -> any CIFilter & CIGlassLozenge](cifilter-swift.class/glasslozenge.md)
  Creates a lozenge-shaped lens and distorts the image.
- [class func holeDistortion() -> any CIFilter & CIHoleDistortion](cifilter-swift.class/holedistortion.md)
  Distorts an image with a circular area that pushes the image outward.
- [class func lightTunnel() -> any CIFilter & CILightTunnel](cifilter-swift.class/lighttunnel.md)
  Distorts an image by generating a light tunnel.
- [class func ninePartStretched() -> any CIFilter & CINinePartStretched](cifilter-swift.class/ninepartstretched.md)
  Distorts an image by stretching it between two breakpoints.
- [class func ninePartTiled() -> any CIFilter & CINinePartTiled](cifilter-swift.class/nineparttiled.md)
  Distorts an image by tiling portions of it.
- [class func pinchDistortion() -> any CIFilter & CIPinchDistortion](cifilter-swift.class/pinchdistortion.md)
  Distorts an image by creating a pinch effect with stronger distortion in the center.
- [class func stretchCrop() -> any CIFilter & CIStretchCrop](cifilter-swift.class/stretchcrop.md)
  Distorts an image by stretching or cropping to fit a specified size.
- [class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion](cifilter-swift.class/toruslensdistortion.md)
  Creates a torus-shaped lens to distort the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/vortexdistortion())*