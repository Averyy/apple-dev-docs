# perspectiveRotate()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Rotates an image in a 3D space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate
```

```objc
+ (CIFilter<CIPerspectiveRotate> *) perspectiveRotateFilter;
```

## Return Value

The adjusted image.

## Discussion

This method applies the perspective rotate filter to an image. The effect rotates the image in 3D space to simulate the observer changing viewing position.

The perspective rotate filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`pitch`**: A `float` representing the adjustment along the pitch axis in 3D space as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`yaw`**: A `float` representing the adjustment along the vertical axis as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`roll`**: A `float` representing the amount of horizontal axis in 3D space as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`focalLength`**: A `float` representing the simulated focal length as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that rotates the image:

```swift
func perspectiveRotate(inputImage: CIImage) -> CIImage {
    let perspectiveRotateFilter = CIFilter.perspectiveRotate()
    perspectiveRotateFilter.inputImage = inputImage
    perspectiveRotateFilter.pitch = 0
    perspectiveRotateFilter.yaw = 0.1
    perspectiveRotateFilter.roll = 0.3
    perspectiveRotateFilter.focalLength = 18
    return perspectiveRotateFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a perspective rotate filter is applied, resulting in the image becoming smaller and rotated.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3582225@2x.png)

## See Also

### Filters
- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](./bicubicscaletransform%28%29.md)
  Produces a high-quality scaled version of an image.
- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](./edgepreserveupsample%28%29.md)
  Creates a high-quality upscaled image.
- [class func keystoneCorrectionCombined() -> any CIFilter & CIKeystoneCorrectionCombined](./keystonecorrectioncombined%28%29.md)
  Adjusts the image vertically and horizontally to remove distortion.
- [class func keystoneCorrectionHorizontal() -> any CIFilter & CIKeystoneCorrectionHorizontal](./keystonecorrectionhorizontal%28%29.md)
  Horizontally adjusts an image to remove distortion.
- [class func keystoneCorrectionVertical() -> any CIFilter & CIKeystoneCorrectionVertical](./keystonecorrectionvertical%28%29.md)
  Vertically adjusts an image to remove distortion.
- [class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform](./lanczosscaletransform%28%29.md)
  Creates a high-quality, scaled version of a source image.
- [class func perspectiveCorrection() -> any CIFilter & CIPerspectiveCorrection](./perspectivecorrection%28%29.md)
  Transforms an image’s perspective.
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](./perspectivetransform%28%29.md)
  Alters an image’s geometry to adjust the perspective.
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](./perspectivetransformwithextent%28%29.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](./straighten%28%29.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/perspectiverotate())*