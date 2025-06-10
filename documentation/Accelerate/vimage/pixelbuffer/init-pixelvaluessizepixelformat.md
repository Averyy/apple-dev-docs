# init(pixelValues:size:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init

Creates a new pixel buffer by copying the supplied collection of pixel values.

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
init<U>(pixelValues: U, size: vImage.Size, pixelFormat: Format.Type = Format.self) where U : AccelerateBuffer, Format.ComponentType == U.Element
```

#### Discussion

## Parameters

- `pixelValues`: The source pixel values.   must contain   elements.
- `size`: The size of the new buffer.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int, pixelFormat: Format.Type)](vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-zwzz.md)
  Returns a new buffer that references existing data.
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int?, pixelFormat: Format.Type)](vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-27czc.md)
  Calculates the correct bytes per row and returns a new buffer that references existing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(pixelvalues:size:pixelformat:))*