# channelCount

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

Returns the number of channels.

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
var channelCount: Int { get }
```

Available when `Format` conforms to `StaticPixelFormat`.

#### Discussion

For example, the following code prints the number of channels in two interleaved buffers:

```swift
 let x = vImage.PixelBuffer<vImage.InterleavedFx2>(size: vImage.Size(width: 1,
                                                                     height: 1))
 let y = vImage.PixelBuffer<vImage.Interleaved8x4>(size: vImage.Size(width: 1,
                                                                     height: 1))

 // Prints "2 4".
 print(x.channelCount, y.channelCount)
```

## See Also

### Inspecting a pixel buffer
- [var width: Int](./width.md)
  The width of the pixel buffer.
- [var height: Int](./height.md)
  The height of the pixel buffer.
- [var size: vImage.Size](./size.md)
  The size of the pixel buffer.
- [var rowStride: Int](./rowstride.md)
  The width, in pixels, of the underlying memory, including any additional row byte padding.
- [var byteCountPerPixel: Int](./bytecountperpixel.md)
  Returns the number of bytes per pixel.
- [var count: Int](./count.md)
  The total number of pixels multiplied by the number of channels in the buffer, including any row padding.
- [var array: [Format.ComponentType]](./array.md)
  An array of `width * height * channelCount` values that’s a copy of the buffer’s visible contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/channelcount)*