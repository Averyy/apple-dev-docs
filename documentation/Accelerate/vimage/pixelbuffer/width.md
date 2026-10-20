# width

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The width of the pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
var width: Int { get }
```

## See Also

### Inspecting a pixel buffer
- [var height: Int](./height.md)
  The height of the pixel buffer.
- [var size: vImage.Size](./size.md)
  The size of the pixel buffer.
- [var channelCount: Int](./channelcount.md)
  Returns the number of channels.
- [var rowStride: Int](./rowstride.md)
  The width, in pixels, of the underlying memory, including any additional row byte padding.
- [var byteCountPerPixel: Int](./bytecountperpixel.md)
  Returns the number of bytes per pixel.
- [var count: Int](./count.md)
  The total number of pixels multiplied by the number of channels in the buffer, including any row padding.
- [var array: [Format.ComponentType]](./array.md)
  An array of `width * height * channelCount` values that’s a copy of the buffer’s visible contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/width)*