# matchedFromWorkingSpace(to:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Returns a new image created by color matching from the context’s working color space to the specified color space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func matchedFromWorkingSpace(to colorSpace: CGColorSpace) -> CIImage?
```

```objc
- (CIImage *) imageByColorMatchingWorkingSpaceToColorSpace:(CGColorSpaceRef) colorSpace;
```

## Return Value

An image object representing the result of the color matching operation, or `nil` if the color spaces to be converted are not compatible.

## Parameters

- `colorSpace`: The color space to be converted to. This color space must conform to the [`CGColorSpaceModel.rgb`](../../CoreGraphics/cgcolorspacemodel/rgb.md) color space model.

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
- [func oriented(forExifOrientation: Int32) -> CIImage](./oriented%28forexiforientation%29.md)
  Returns a new image created by transforming the original image to the specified EXIF orientation.
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
- [func premultiplyingAlpha() -> CIImage](./premultiplyingalpha%28%29.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](./unpremultiplyingalpha%28%29.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](./settingalphaone%28in%29.md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/matchedfromworkingspace(to:))*