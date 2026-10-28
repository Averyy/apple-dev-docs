# lanczosScaleTransform()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a high-quality, scaled version of a source image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform
```

```objc
+ (CIFilter<CILanczosScaleTransform> *) lanczosScaleTransformFilter;
```

## Mentions

- [Processing an Image Using Built-in Filters](../processing-an-image-using-built-in-filters.md)

## Return Value

The adjusted image.

## Discussion

This method applies the Lanczos scale transform filter to an image. The effect creates the output image by scaling the input image based on the scale and aspect ratio properties provided.

The Lanczos scale filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`scale`**: A `float` representing the scaling factor used on the image as an [`NSNumber`](../../Foundation/nsnumber.md). Values less than `1.0` scale down the images. Values greater than `1.0` scale up the image.
- **`aspectRatio`**: A `float` representing the additional horizontal scaling factor used on the image as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that results in a smaller scaled image with high quality:

```swift
func lanczosScale(inputImage: CIImage) -> CIImage {    
    let lanczosScaleFilter = CIFilter.lanczosScaleTransform()
    lanczosScaleFilter.inputImage = inputImage
    lanczosScaleFilter.scale =  0.3
    lanczosScaleFilter.aspectRatio = 1
    return lanczosScaleFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a Lanczos scale transform filter is applied, resulting in a scaled-down or smaller image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3582221@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/lanczosscaletransform())*