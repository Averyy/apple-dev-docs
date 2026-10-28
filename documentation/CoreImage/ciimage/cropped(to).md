# cropped(to:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Returns a new image with a cropped portion of the original image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func cropped(to rect: CGRect) -> CIImage
```

```objc
- (CIImage *) imageByCroppingToRect:(CGRect) rect;
```

## Return Value

An image object cropped to the specified rectangle.

## Discussion

![Butterfly photo with background cropped out](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-2951307@2x.png)

## Discussion

Due to Core Image’s coordinate system mismatch with [UIKit](https://developer.apple.com/library/archive/releasenotes/General/WhatsNewIniOS/Articles/iOS5.html#//apple_ref/doc/uid/TP30915195-SW41), this filtering approach may yield unexpected results when displayed in a [`UIImageView`](../../UIKit/uiimageview.md) with [`contentMode`](../../UIKit/uiview/contentmode-swift.property.md). Be sure to back it with a [`cgImage`](./cgimage.md) so that it handles [`contentMode`](../../UIKit/uiview/contentmode-swift.property.md) properly.

```swift
CIContext* context = [CIContext context];
CGImageRef cgCroppedImage = [context createCGImage:ciCroppedImage fromRect:ciCroppedImage.extent];
UIImage* croppedImage = [UIImage imageWithCGImage:cgCroppedImage];
CGImageRelease(cgCroppedImage);
```

If you are displaying or processing your image primarily as a [`CGImage`](../../CoreGraphics/cgimage.md) or [`UIImage`](../../UIKit/uiimage.md), with no additional Core Image application, consider cropping in Core Graphics using the [`cropping(to:)`](../../CoreGraphics/cgimage/cropping%28to%29.md) function to save processing overhead from conversion of images to [`CIImage`](../ciimage.md).  It makes most sense to use [`cropped(to:)`](./cropped%28to%29.md) when you already have [`CIImage`](../ciimage.md) in your pipeline.

## Parameters

- `rect`: The rectangle, in image coordinates, to which to crop the image.

## See Also

### Creating an Image by Modifying an Existing Image
- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](./applyingfilter%28_,parameters%29.md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func applyingFilter(String) -> CIImage](./applyingfilter%28_%29.md)
  Applies the filter to an image and returns the output.
- [func transformed(by: CGAffineTransform) -> CIImage](./transformed%28by%29.md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](./transformed%28by,highqualitydownsample%29.md)
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
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](./matchedfromworkingspace%28to%29.md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](./premultiplyingalpha%28%29.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](./unpremultiplyingalpha%28%29.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](./settingalphaone%28in%29.md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/cropped(to:))*