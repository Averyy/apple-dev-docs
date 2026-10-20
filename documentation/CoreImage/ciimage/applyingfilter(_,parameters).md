# applyingFilter(_:parameters:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Returns a new image created by applying a filter to the original image with the specified name and parameters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func applyingFilter(_ filterName: String, parameters params: [String : Any]) -> CIImage
```

```objc
- (CIImage *) imageByApplyingFilter:(NSString *) filterName withInputParameters:(NSDictionary<NSString *,id> *) params;
```

#### Return Value

An image object representing the result of applying the filter.

#### Discussion

Calling this method is equivalent to the following sequence of steps:

1. Creating a [`CIFilter`](../cifilter-swift.class.md) instance
2. Setting the original image as the filter’s `inputImage` parameter
3. Setting the remaining filter parameters from the `params` dictionary
4. Retrieving the [`outputImage`](../cifilter-swift.class/outputimage.md) object from the filter

> ❗ **Important**:  This method, though convenient, is inefficient if used multiple times in succession. Achieve better performance by chaining filters without asking for the outputs of individual filters. For more information, see [Processing an Image Using Built-in Filters](../processing-an-image-using-built-in-filters.md).

## Parameters

- `filterName`: The name of the filter to apply, as used when creating a [`CIFilter`](../cifilter-swift.class.md) instance with the [`init(name:)`](../cifilter-swift.class/init%28name%29.md) method.
- `params`: A dictionary whose key-value pairs are set as input values to the filter. Each key is a constant that specifies the name of an input parameter for the filter, and the corresponding value is the value for that parameter. See [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346) for built-in filters and their allowed parameters.

## See Also

### Creating an Image by Modifying an Existing Image
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
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](./matchedfromworkingspace%28to%29.md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](./premultiplyingalpha%28%29.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](./unpremultiplyingalpha%28%29.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](./settingalphaone%28in%29.md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/applyingfilter(_:parameters:))*