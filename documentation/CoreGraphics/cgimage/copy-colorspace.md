# copy(colorSpace:)

**Framework**: Core Graphics  
**Kind**: method

Creates a copy of a bitmap image, replacing its colorspace.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copy(colorSpace space: CGColorSpace) -> CGImage?
```

#### Return Value

A new CGImage that is a copy of the image passed as the `image` parameter but with its color space replaced by that specified by the `colorspace` parameter. Returns `NULL` if `image` is an image mask, or if the number of components of `colorspace` is not the same as the number of components of the colorspace of `image`. In Objective-C, you’re responsible for releasing this object using [`CGImageRelease`](cgimagerelease.md).

## Parameters

- `space`: The destination color space. The number of components in this color space must be the same as the number in the specified image.

## See Also

- [func copy() -> CGImage?](cgimage/copy.md)
  Creates a copy of a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/copy(colorspace:))*