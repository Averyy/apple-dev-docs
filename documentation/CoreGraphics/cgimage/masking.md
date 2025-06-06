# masking(_:)

**Framework**: Core Graphics  
**Kind**: method

Creates a bitmap image from an existing image and an image mask.

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
func masking(_ mask: CGImage) -> CGImage?
```

#### Return Value

An image created by masking `image` with `mask`. In Objective-C, you’re responsible for releasing this object by calling [`CGImageRelease`](cgimagerelease.md).

#### Discussion

The resulting image depends on whether the `mask` parameter is an image mask or an image. If the `mask` parameter is an image mask, then the source samples of the image mask act as an inverse alpha value. That is, if the value of a source sample in the image mask is S, then the corresponding region in `image` is blended with the destination using an alpha value of (1-S). For example, if S is 1, then the region is not painted, while if S is 0, the region is fully painted.

If the `mask` parameter is an image, then it serves as an alpha mask for blending the image onto the destination. The source samples of `mask`’ act as an alpha value. If the value of the source sample in mask is S, then the corresponding region in image is blended with the destination with an alpha of S. For example, if S is 0, then the region is not painted, while if S is 1, the region is fully painted.

## Parameters

- `mask`: A mask. If the mask is an image, it must be in the DeviceGray color space, must not have an alpha component, and may not itself be masked by an image mask or a masking color. If the mask is not the same size as the image specified by the   parameter, the mask is scaled to fit the image.

## See Also

- [func cropping(to: CGRect) -> CGImage?](cgimage/cropping(to:).md)
  Creates a bitmap image using the data contained within a subregion of an existing bitmap image.
- [func copy(maskingColorComponents: [CGFloat]) -> CGImage?](cgimage/copy(maskingcolorcomponents:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/masking(_:))*