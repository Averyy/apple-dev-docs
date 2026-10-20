# glassLozenge()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a lozenge-shaped lens and distorts the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func glassLozenge() -> any CIFilter & CIGlassLozenge
```

```objc
+ (CIFilter<CIGlassLozenge> *) glassLozengeFilter;
```

#### Return Value

The distorted image.

#### Discussion

This method applies the glass lozenge filter to an image. This effect distorts an image by creating a lozenge shape placed over the input image.

The absolute threshold filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`radius`**: A `float` representing the radius of the lozenge distortion as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`refraction`**: A `float` representing the refraction of the glass as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`inputPoint1`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the x and y positions that define the center of the circle at the first end of the lozenge.
- **`inputPoint2`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the x and y positions that define the center of the circle at the second end of the lozenge.

The following code creates a filter that results in a large glass lozenge distorting the image:

```swift
func glassLozenge(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.glassLozenge()
    filter.inputImage = inputImage
    filter.refraction = 1.7
    filter.point0 = CGPoint(x: 150, y: 1050)
    filter.point1 = CGPoint(x: 3050, y: 150)
    return filter.outputImage!
}
```

![Two images next to each other. The left image contains a photograph of three hydrangea flowers with leaves in the background. In the right image, the glass lozenge filter has been applied. It appears as if the glass pill shape has been placed on top of the image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407280@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/glasslozenge())*