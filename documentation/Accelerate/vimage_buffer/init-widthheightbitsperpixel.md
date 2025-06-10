# init(width:height:bitsPerPixel:)

**Framework**: Accelerate  
**Kind**: init

Creates a new buffer with the specified width, height, and bits per pixel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
init(width: Int, height: Int, bitsPerPixel: UInt32) throws
```

## Mentions

- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)

#### Discussion

This function allocates a buffer’s memory, but doesn’t initialize the memory.

## Parameters

- `width`: The width of the buffer, in pixels.
- `height`: The height of the buffer, in pixels.
- `bitsPerPixel`: The number of bits in a single pixel.

## See Also

- [init(size: CGSize, bitsPerPixel: UInt32) throws](vimage_buffer/init(size:bitsperpixel:).md)
  Creates a new buffer with the specified size and bits per pixel.
- [init()](vimage_buffer/init.md)
  Creates an empty vImage buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/init(width:height:bitsperpixel:))*