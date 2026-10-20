# init(pixelValues:size:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a new pixel buffer by copying the supplied collection of pixel values.

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
init<U>(pixelValues: U, size: vImage.Size, pixelFormat: Format.Type = Format.self) where U : AccelerateBuffer, Format.ComponentType == U.Element
```

Available when `Format` conforms to `StaticPixelFormat`.

#### Discussion

## Parameters

- `pixelValues`: The source pixel values. `pixelValues` must contain `size.width * size.height * channelCount` elements.
- `size`: The size of the new buffer.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

### Creating a pixel buffer from raw pixel data
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int, pixelFormat: Format.Type)](./init%28data,width,height,bytecountperrow,pixelformat%29-zwzz.md)
  Returns a new buffer that references existing data.
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int?, pixelFormat: Format.Type)](./init%28data,width,height,bytecountperrow,pixelformat%29-27czc.md)
  Calculates the correct bytes per row and returns a new buffer that references existing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(pixelvalues:size:pixelformat:))*