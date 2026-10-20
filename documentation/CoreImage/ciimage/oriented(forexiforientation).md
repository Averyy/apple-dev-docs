# oriented(forExifOrientation:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Returns a new image created by transforming the original image to the specified EXIF orientation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func oriented(forExifOrientation orientation: Int32) -> CIImage
```

```objc
- (CIImage *) imageByApplyingOrientation:(int) orientation;
```

#### Return Value

An image object representing the result of rotating or mirroring the image to the target orientation.

#### Discussion

This method determines and then applies the transformation needed to reorient the image to the specified orientation. If you plan to also apply other transformations, you can retrieve the transformation this method would use by calling the [`orientationTransform(forExifOrientation:)`](./orientationtransform%28forexiforientation%29.md) method.

## Parameters

- `orientation`: An integer specifying an image orientation according to the EXIF specification. For details, see [`kCGImagePropertyOrientation`](../../ImageIO/kcgimagepropertyorientation.md).

## See Also

### Creating an Image by Modifying an Existing Image
- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](./applyingfilter%28_,parameters%29.md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func applyingFilter(String) -> CIImage](./applyingfilter%28_%29.md)
  Applies the filter to an image and returns the output.
- [func transformed(by: CGAffineTransform) -> CIImage](./transformed%28by%29.md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](./transformed%28by,highqualitydownsample%29.md)
- [func cropped(to: CGRect) -> CIImage](./cropped%28to%29.md)
  Returns a new image with a cropped portion of the original image.
- [func clampedToExtent() -> CIImage](./clampedtoextent%28%29.md)
  Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [func clamped(to: CGRect) -> CIImage](./clamped%28to%29.md)
  Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [func composited(over: CIImage) -> CIImage](./composited%28over%29.md)
  Returns a new image created by compositing the original image over the specified destination image.
- [func convertingWorkingSpaceToLab() -> CIImage](./convertingworkingspacetolab%28%29.md)
- [func convertingLabToWorkingSpace() -> CIImage](./convertinglabtoworkingspace%28%29.md)
- [func matchedToWorkingSpace(from: CGColorSpace) -> CIImage?](./matchedtoworkingspace%28from%29.md)
  Returns a new image created by color matching from the specified color space to the context’s working color space.
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](./matchedfromworkingspace%28to%29.md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](./premultiplyingalpha%28%29.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](./unpremultiplyingalpha%28%29.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](./settingalphaone%28in%29.md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/oriented(forexiforientation:))*