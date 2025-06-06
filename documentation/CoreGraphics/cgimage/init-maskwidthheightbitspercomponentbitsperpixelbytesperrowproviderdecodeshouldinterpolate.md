# init(maskWidth:height:bitsPerComponent:bitsPerPixel:bytesPerRow:provider:decode:shouldInterpolate:)

**Framework**: Core Graphics  
**Kind**: init

Creates a bitmap image mask from data supplied by a data provider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(maskWidth width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool)
```

#### Return Value

A bitmap image mask. In Objective-C, you’re responsible for releasing this object by calling [`CGImageRelease`](cgimagerelease.md).

#### Discussion

A bitmap image mask is used the same way an artist uses a silkscreen, or a sign painter uses a stencil. The bitmap represents a mask through which a color is transferred. The bitmap itself does not have a color. It gets its color from the fill color currently set in the graphics state.

When you draw into a context with a bitmap image mask, the mask determines where and how the current fill color is applied to the image rectangle. Each sample value in the mask specifies how much of the current fill color is masked out at a specific location. Effectively, the sample value specifies the opacity of the mask. Larger values represent greater opacity and hence less color applied to the page.

Image masks must be 1, 2, 4, or 8 bits per component. For a 1-bit mask, a sample value of `1` specifies sections of the mask that are masked out; these sections block the current fill color. A sample value of `0` specifies sections of the mask that are not masked out; these sections show the current fill color of the graphics state when the mask is painted. You can think of the sample values as an inverse alpha. That is, a value of `1` is transparent and `0` is opaque.

For image masks that are 2, 4, or 8 bits per component, each component is mapped to a range of 0 to 1 by scaling using this formula:

`1/(2^bits per component – 1)`

For example, a 4-bit mask has values that range from 0 to 15. These values are scaled by 1/15 so that each component ranges from 0 to 1. Component values that rescale to 0 or 1 behave the same way as they behave for 1-bit image masks. Values that scale to between 0 and 1 act as an inverse alpha. That is, the fill color is painted as if it has an alpha value of (`1 – MaskSampleValue`). For example, if the sample value of an 8-bit mask scales to `0.8`, the current fill color is painted as if it has an alpha value of `0.2`, that is (`1–0.8`).

## Parameters

- `width`: The width, in pixels, of the required image mask.
- `height`: The height, in pixels, of the required image mask.
- `bitsPerComponent`: The number of significant masking bits in a source pixel. For example, if the source image is an 8-bit mask, you specify 8 bits per component. Image masks must be 1, 2, 4, or 8 bits per component.
- `bitsPerPixel`: The total number of bits in a source pixel.
- `bytesPerRow`: The number of bytes to use for each horizontal row of the image mask.
- `provider`: The data source for the image mask.
- `decode`: Typically a decode array is unnecessary, and you should pass  .
- `shouldInterpolate`: A Boolean value that specifies whether an edge-smoothing algorithm is applied to the image mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/init(maskwidth:height:bitspercomponent:bitsperpixel:bytesperrow:provider:decode:shouldinterpolate:))*