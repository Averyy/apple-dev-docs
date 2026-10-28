# droste()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (CIFilter<CIDroste> *) drosteFilter;
```

## Return Value

The distorted image.

## Discussion

This method applies the Droste filter to an image. This effect creates a Droste effect that distorts the image by repeating smaller versions of the same image within itself.

The Droste filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`rotation`**: A `float` representing the angle of the rotation, in radians, as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`zoom`**: A `float` representing the zoom of the effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`periodicity`**: A float representing the amount of intervals as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`inputInsetPoint1`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the x and y position that defines the first inset point.
- **`inputInsetPoint0`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the x and y position that defines the second inset point.
- **`inputStrands`**: A float representing the amount of strands as an [`NSNumber`](../../Foundation/nsnumber.md).

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

![Two images arranged horizontally. The left image contains a photograph of a vineyard with a partially cloudy sky. The right image shows the result of applying a Droste filter. A portion of the image has been rotated and then repeatedly scaled.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407275@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/droste())*