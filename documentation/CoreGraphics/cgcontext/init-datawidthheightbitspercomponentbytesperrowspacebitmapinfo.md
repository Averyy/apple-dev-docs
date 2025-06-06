# init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:)

**Framework**: Core Graphics  
**Kind**: init

Creates a bitmap graphics context.

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
init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32)
```

#### Return Value

A new bitmap context, or `nil` if a context could not be created. In Objective-C, you’re responsible for releasing this object using [`CGContextRelease`](cgcontextrelease.md).

#### Discussion

When you draw into this context, Core Graphics renders your drawing as bitmapped data in the specified block of memory.

The pixel format for a new bitmap context is determined by three parameters—the number of bits per component, the color space, and an alpha option (expressed as a [`CGBitmapInfo`](cgbitmapinfo.md) constant). The alpha value determines the opacity of a pixel when it is drawn.

## Parameters

- `data`: Pass   if you want this function to allocate memory for the bitmap. This frees you from managing your own memory, which reduces memory leak issues.
- `width`: The width, in pixels, of the required bitmap.
- `height`: The height, in pixels, of the required bitmap.
- `bitsPerComponent`: The number of bits to use for each component of a pixel in memory. For example, for a 32-bit pixel format and an RGB color space, you would specify a value of 8 bits per component. For the list of supported pixel formats, see “Supported Pixel Formats” in the   chapter of  .
- `bytesPerRow`: The number of bytes of memory to use per row of the bitmap. If the   parameter is  , passing a value of   causes the value to be calculated automatically.
- `space`: The color space to use for the bitmap context. Note that indexed color spaces are not supported for bitmap graphics contexts.
- `bitmapInfo`: For an example of how to specify the color space, bits per pixel, bits per pixel component, and bitmap information, see  .

## See Also

- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32, releaseCallback: CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)](cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:releasecallback:releaseinfo:).md)
  Creates a bitmap graphics context with the specified callback function.
- [typealias CGBitmapContextReleaseDataCallback](cgbitmapcontextreleasedatacallback.md)
  A callback function used to release data associate with the bitmap context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:))*