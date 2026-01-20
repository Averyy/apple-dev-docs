# droste()

**Framework**: Core Image  
**Kind**: method

Stylizes an image with the Droste effect.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func droste() -> any CIFilter & CIDroste
```

#### Return Value

The distorted image.

#### Discussion

This method applies the Droste filter to an image. This effect creates a Droste effect that distorts the image by repeating smaller versions of the same image within itself.

The Droste filter uses the following properties:

The following code creates a filter that results in the image becoming a repeated, scaled pattern:

```swift
func drosteFilter(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.droste()
    filter.inputImage = inputImage
    filter.insetPoint1 = CGPoint(
        x: inputImage.extent.size.width * 0.2,
        y: inputImage.extent.size.height * 0.2
    )
    filter.insetPoint0 = CGPoint(
        x: inputImage.extent.size.width * 0.8,
        y: inputImage.extent.size.height * 0.8
    )
    filter.periodicity = 1
    filter.rotation = 0
    filter.strands = 1
    filter.zoom = 1
    return filter.outputImage!.cropped(to: inputImage.extent)
}
```

![Two images arranged horizontally. The left image contains a photograph of a vineyard with a partially cloudy sky. The right image shows the result of applying a Droste filter. A portion of the image has been rotated and then repeatedly scaled.](https://docs-assets.developer.apple.com/published/5199556d6ce6d0dfbf643d23a2d24423/media-4407275%402x.png)

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
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](cifilter-swift.class/twirldistortion.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/droste())*