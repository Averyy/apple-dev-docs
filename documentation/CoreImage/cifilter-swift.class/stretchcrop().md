# stretchCrop()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Distorts an image by stretching or cropping to fit a specified size.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func stretchCrop() -> any CIFilter & CIStretchCrop
```

```objc
+ (CIFilter<CIStretchCrop> *) stretchCropFilter;
```

## Return Value

The distorted image.

## Discussion

This method applies the stretch crop filter to an image. This effect distorts an image by stretching an image and then applies the crop extent. If the crop value is 0, the filter only uses stretching. If the value is 1, then the filter only uses cropping.

The stretch crop filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`centerStretchAmount`**: A `float` representing the amount of stretching of the center of the image as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`size`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) representing the desired size of the output image.
- **`cropAmount`**: A `float` representing the amount of cropping you apply to achieve the target size as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that results in a smaller image that’s distorted and cropped to be the defined size:

```swift
func stretchCrop(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.stretchCrop()
    filter.inputImage = inputImage
    filter.cropAmount = 0.25
    filter.centerStretchAmount = 0.25
    filter.size = CGPoint(
        x: inputImage.extent.width * 2,
        y: inputImage.extent.size.height * 0.8
    )
    return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photograph of the Golden Gate Bridge with a clear sky in the background. The right image shows the result of applying the stretch crop filter. The image has been stretched in the horizontal direction and cropped in the vertical direction.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407279@2x.png)

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
- [class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion](./toruslensdistortion%28%29.md)
  Creates a torus-shaped lens to distort the image.
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](./twirldistortion%28%29.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/stretchcrop())*