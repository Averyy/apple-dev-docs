# cropping(to:)

**Framework**: Core Graphics  
**Kind**: method

Creates a bitmap image using the data contained within a subregion of an existing bitmap image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cropping(to rect: CGRect) -> CGImage?
```

#### Return Value

A [`CGImage`](cgimage.md) object that specifies a subimage of the image. If the `rect` parameter defines an area that is not in the image, returns `NULL`.

#### Discussion

Cropping removes content around the designated rectangle; it cuts out the desired area of the input image and returns an image of the cropped size.

![Butterfly photo with background cropped out](https://docs-assets.developer.apple.com/published/44e39ae57f70286b7a3ea4d5a6491b8b/media-2951298%402x.png)

[`cropping(to:)`](cgimage/cropping(to:).md) performs the following tasks to create the subimage:

- It calls the [`CGRectIntegral(_:)`](cgrectintegral(_:).md) function to adjust the `rect` parameter to integral bounds.
- It intersects the `rect` with a rectangle whose origin is `(0,0)` and size is equal to the size of the image specified by the `image` parameter.
- It reads the pixels within the resulting rectangle, treating the first pixel within as the origin of the subimage.

If `W` and `H` are the width and height of image, respectively, then the point `(0,0)` corresponds to the first pixel of the image data. The point `(W–1, 0)` is the last pixel of the first row of the image data, while `(0, H–1)` is the first pixel of the last row of the image data and `(W–1, H–1)` is the last pixel of the last row of the image data.

> ❗ **Important**:  Be sure to specify the subrectangle’s coordinates relative to the original image’s full size, even if the [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView) shows only a scaled version.

The resulting image retains a reference to the original image, which means you may release the original image after calling this function.  In Swift, you do not need to release the original image reference explicitly.

If you already use [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage), or if you are post-processing images as [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage) data in Core Image, such as chaining together multiple filters to the cropped result, it may be more efficient to crop [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage) directly in the Core Image framework using the `CICrop` filter; in this case, use the convenience function [`cropped(to:)`](https://developer.apple.com/documentation/CoreImage/CIImage/cropped(to:)).

## Parameters

- `rect`: A rectangle specifying the portion of the image to keep.

## See Also

- [func masking(CGImage) -> CGImage?](cgimage/masking(_:).md)
  Creates a bitmap image from an existing image and an image mask.
- [func copy(maskingColorComponents: [CGFloat]) -> CGImage?](cgimage/copy(maskingcolorcomponents:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/cropping(to:))*