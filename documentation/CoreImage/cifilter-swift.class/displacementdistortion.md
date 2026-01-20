# displacementDistortion()

**Framework**: Core Image  
**Kind**: method

Applies the grayscale values of the second image to the first image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func displacementDistortion() -> any CIFilter & CIDisplacementDistortion
```

#### Return Value

The distorted image.

#### Discussion

This method applies the displacement distortion filter to an image. This effect distorts an image by applying the grayscale color values of the texture image.

The displacement distortion filter uses the following properties:

The following code creates a filter that applies the grayscale values of the displacement image to the input image:

```swift
func displacementDistortion(inputImage: CIImage) -> CIImage {
    // Create an interesting grayscale pattern.
    let displacementImage = CIFilter.checkerboardGenerator()
    displacementImage.color0 = CIColor.white
    displacementImage.color1 = CIColor.black
    displacementImage.width = 200
    let gaussianBlur = CIFilter.gaussianBlur()
    gaussianBlur.radius = 40
    gaussianBlur.inputImage = displacementImage.outputImage
    // Use it in the displacement filter.
    let filter = CIFilter.displacementDistortion()
    filter.displacementImage = gaussianBlur.outputImage
    filter.inputImage = inputImage
    filter.scale = 1000
    return filter.outputImage!
}
```

![A group of three images: two images on the left arranged vertically and a third image on the right vertically centered. The top left image is of a modern concrete building with black tinted windows. The bottom left image is a blurred checkerboard pattern. The image on the right shows the result of applying the displacement distortion effect. It appears as if there is a ripple in the image.](https://docs-assets.developer.apple.com/published/2ca5fc058edc7840ca1f56e318dd486b/media-4407313%402x.png)

## See Also

- [class func bumpDistortion() -> any CIFilter & CIBumpDistortion](cifilter-swift.class/bumpdistortion.md)
  Distorts an image with a concave or convex bump.
- [class func bumpDistortionLinear() -> any CIFilter & CIBumpDistortionLinear](cifilter-swift.class/bumpdistortionlinear.md)
  Linearly distorts an image with a concave or convex bump.
- [class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion](cifilter-swift.class/circlesplashdistortion.md)
  Distorts an image with radiating circles to the periphery of the image.
- [class func circularWrap() -> any CIFilter & CICircularWrap](cifilter-swift.class/circularwrap.md)
  Distorts an image by increasing the distance of the center of the image.
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
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](cifilter-swift.class/twirldistortion.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/displacementdistortion())*