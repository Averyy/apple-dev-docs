# keystoneCorrectionVertical()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Vertically adjusts an image to remove distortion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func keystoneCorrectionVertical() -> any CIFilter & CIKeystoneCorrectionVertical
```

```objc
+ (CIFilter<CIKeystoneCorrectionVertical> *) keystoneCorrectionVerticalFilter;
```

## Return Value

The adjusted image.

## Discussion

This method applies the keystone correction vertical. The effect performs vertical adjustment of the image to shape the image to be rectangular. This effect is commonly used with multimedia projectors to correct the distortion caused by the projector being lower or higher than the projected screen.

The keystone vertical filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`topLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the top-left corner of the output image.
- **`topRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the top-right corner of the output image.
- **`bottomLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the bottom-left corner of the output image.
- **`bottomRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the bottom-right corner of the output image.
- **`focalLength`**: A `float` representing the simulated focal length as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that distorts the image:

```swift
func keystoneCorrectionVertical(inputImage: CIImage) -> CIImage {
    let keystoneCorrect = CIFilter.keystoneCorrectionVertical()
    keystoneCorrect.inputImage = inputImage
    keystoneCorrect.topLeft = CGPoint(x: 0, y: 3024)
    keystoneCorrect.topRight = CGPoint(x: 4032, y: 3024)
    keystoneCorrect.bottomLeft = CGPoint(x: 200, y: 0)
    keystoneCorrect.bottomRight = CGPoint(x: 4032, y: 0)
    keystoneCorrect.focalLength = 18
    return keystoneCorrect.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a keystone correction vertical filter is applied, distorting the rectangular image to appear slanted with the bottom-left corner of the photo raised.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3582222@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/keystonecorrectionvertical())*