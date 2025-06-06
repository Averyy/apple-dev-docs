# init(jpegDataProviderSource:decode:shouldInterpolate:intent:)

**Framework**: Core Graphics  
**Kind**: init

Creates a bitmap image using JPEG-encoded data supplied by a data provider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(jpegDataProviderSource source: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)
```

#### Return Value

A new CGImage. In Objective-C, you’re responsible for releasing this object by calling [`CGImageRelease`](cgimagerelease.md).

## Parameters

- `source`: A data provider supplying JPEG-encoded data.
- `decode`: The decode array for the image. Typically a decode array is unnecessary, and you should pass  .
- `shouldInterpolate`: A Boolean value that specifies whether interpolation should occur. The interpolation setting specifies whether a pixel-smoothing algorithm should be applied to the image.
- `intent`: A CGColorRenderingIntent constant that specifies how to handle colors that are not located within the gamut of the destination color space of a graphics context.

## See Also

- [init?(width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](cgimage/init(width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:).md)
  Creates a bitmap image from data supplied by a data provider.
- [init?(pngDataProviderSource: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](cgimage/init(pngdataprovidersource:decode:shouldinterpolate:intent:).md)
  Creates a bitmap image using PNG-encoded data supplied by a data provider.
- [init?(headroom: Float, width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](cgimage/init(headroom:width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/init(jpegdataprovidersource:decode:shouldinterpolate:intent:))*