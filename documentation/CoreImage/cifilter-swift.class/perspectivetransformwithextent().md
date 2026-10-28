# perspectiveTransformWithExtent()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Alters an image’s geometry to adjust the perspective while applying constraints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent
```

```objc
+ (CIFilter<CIPerspectiveTransformWithExtent> *) perspectiveTransformWithExtentFilter;
```

## Return Value

The adjusted image.

## Discussion

This method applies the perspective transform with extent filter to an image. The effect alters the geometry of an image to simulate the observer changing viewing position. The extent filter crops the image within the bounds specified. You can use the perspective filter to skew an image.

The perspective transform with extent filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`topLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the top-left corner of the output image.
- **`topRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the top-right corner of the output image.
- **`bottomLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the bottom-left corner of the output image.
- **`bottomRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) in the input image mapped to the bottom-right corner of the output image.
- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) representing the dimensions of the output image.

The following code creates a filter that changes the perspective of the input image:

```swift
func perspectiveTransformWithExtent(inputImage: CIImage) -> CIImage {
    let perspectiveTransformFilter = CIFilter.perspectiveTransformWithExtent()
    perspectiveTransformFilter.inputImage = inputImage
    perspectiveTransformFilter.topLeft = CGPoint(x: 100, y: 3984)
    perspectiveTransformFilter.topRight = CGPoint(x: 3732, y: 3025)
    perspectiveTransformFilter.bottomLeft = CGPoint(x: 0, y: 500)
    perspectiveTransformFilter.bottomRight = CGPoint(x: 4032, y: 120)
    perspectiveTransformFilter.extent = CGRect(x: 0, y: 0, width: 3800, height: 3200)
    return perspectiveTransformFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a perspective transform is applied, resulting in it appearing as though the photograph was taken from a different angle.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3582226@2x.png)

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
- [class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate](./perspectiverotate%28%29.md)
  Rotates an image in a 3D space.
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](./perspectivetransform%28%29.md)
  Alters an image’s geometry to adjust the perspective.
- [class func straighten() -> any CIFilter & CIStraighten](./straighten%28%29.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/perspectivetransformwithextent())*