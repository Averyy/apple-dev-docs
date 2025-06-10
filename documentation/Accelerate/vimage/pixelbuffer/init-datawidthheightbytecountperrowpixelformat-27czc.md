# init(data:width:height:byteCountPerRow:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init

Calculates the correct bytes per row and returns a new buffer that references existing data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int? = nil, pixelFormat: Format.Type = Format.self)
```

#### Discussion

Pass `nil` to `byteCountPerRow` to have the function calculate the bytes per row as `width * MemoryLayout<T.ComponentType>.stride * T.channelCount`.

For example, the following code creates a 32-bit planar pixel buffer:

```swift
 let data = UnsafeMutableBufferPointer<Float>.allocate(capacity: 10)
 _ = data.initialize(from: [0, 1, 2, 3, 4,
                            5, 6, 7, 8, 9] as [Float])
 defer {
     data.deallocate()
 }

 let src = vImage.PixelBuffer(data: data.baseAddress!,
                              width: 5,
                              height: 2,
                              byteCountPerRow: nil,
                              pixelFormat: vImage.PlanarF.self)

 // Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]"
 print(src.array)
```

> ❗ **Important**:  The pixel buffer is valid only for the lifetime of `data`.

## Parameters

- `data`: A pointer to the top-left pixel of the buffer.
- `width`: The width, in pixels, of the pixel buffer.
- `height`: The height, in pixels, of the pixel buffer.
- `byteCountPerRow`: The number of bytes in a pixel row.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

- [init<U>(pixelValues: U, size: vImage.Size, pixelFormat: Format.Type)](vimage/pixelbuffer/init(pixelvalues:size:pixelformat:).md)
  Creates a new pixel buffer by copying the supplied collection of pixel values.
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int, pixelFormat: Format.Type)](vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-zwzz.md)
  Returns a new buffer that references existing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-27czc)*