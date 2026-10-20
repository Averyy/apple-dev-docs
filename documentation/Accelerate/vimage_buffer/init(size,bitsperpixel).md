# init(size:bitsPerPixel:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a new buffer with the specified size and bits per pixel.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
init(size: CGSize, bitsPerPixel: UInt32) throws
```

#### Discussion

This function allocates a buffer’s memory, but doesn’t initialize the memory.

## Parameters

- `size`: The size of the buffer, in pixels.
- `bitsPerPixel`: The number of bits in a single pixel.

## See Also

### Creating an empty vImage buffer
- [init(width: Int, height: Int, bitsPerPixel: UInt32) throws](./init%28width,height,bitsperpixel%29.md)
  Creates a new buffer with the specified width, height, and bits per pixel.
- [init()](./init%28%29.md)
  Creates an empty vImage buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/init(size:bitsperpixel:))*