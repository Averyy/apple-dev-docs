# keystoneCorrectionCombined()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Adjusts the image vertically and horizontally to remove distortion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func keystoneCorrectionCombined() -> any CIFilter & CIKeystoneCorrectionCombined
```

```objc
+ (CIFilter<CIKeystoneCorrectionCombined> *) keystoneCorrectionCombinedFilter;
```

## Return Value

The adjusted image.

## Discussion

This method applies the keystone correction combined filter to an image. The effect applies a combined set of horizontal and vertical guides to adjust the shape of the input image. This effect is commonly used when cropping an image to correct distortion. In the figure below, both vertical and horizontal adjustments are made, resulting in a trapezoid-shaped image.

The keystone correction filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`topLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the top-left corner of the output image.
- **`topRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the top-right corner of the output image.
- **`bottomLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the bottom-left corner of the output image.
- **`bottomRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the bottom-right corner of the output image.
- **`focalLength`**: A `float` representing the simulated focal length as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that distorts the image:

```swift
func keystoneCorrectionCombined(inputImage: CIImage) -> CIImage {
    let keystoneCorrect = CIFilter.keystoneCorrectionCombined()
    keystoneCorrect.inputImage = inputImage
    keystoneCorrect.topLeft = CGPoint(x: 0, y: 2448)
    keystoneCorrect.topRight = CGPoint(x: 3164, y: 2248)
    keystoneCorrect.bottomLeft = CGPoint(x: 0, y: 0)
    keystoneCorrect.bottomRight = CGPoint(x: 3164, y: 150)
    keystoneCorrect.focalLength = 35
    return keystoneCorrect.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a keystone correction combined filter is applied, distorting the rectangular image to become a trapezoid.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3582223@2x.png)

## See Also

### Filters
- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](./bicubicscaletransform%28%29.md)
  Produces a high-quality scaled version of an image.
- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](./edgepreserveupsample%28%29.md)
  Creates a high-quality upscaled image.
- [class func keystoneCorrectionHorizontal() -> any CIFilter & CIKeystoneCorrectionHorizontal](./keystonecorrectionhorizontal%28%29.md)
  Horizontally adjusts an image to remove distortion.
- [class func keystoneCorrectionVertical() -> any CIFilter & CIKeystoneCorrectionVertical](./keystonecorrectionvertical%28%29.md)
  Vertically adjusts an image to remove distortion.
- [class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform](./lanczosscaletransform%28%29.md)
  Creates a high-quality, scaled version of a source image.
- [class func perspectiveCorrection() -> any CIFilter & CIPerspectiveCorrection](./perspectivecorrection%28%29.md)
  Transforms an image’s perspective.
- [class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate](./perspectiverotate%28%29.md)
  Rotates an image in a 3D space.
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](./perspectivetransform%28%29.md)
  Alters an image’s geometry to adjust the perspective.
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](./perspectivetransformwithextent%28%29.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](./straighten%28%29.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/keystonecorrectioncombined())*