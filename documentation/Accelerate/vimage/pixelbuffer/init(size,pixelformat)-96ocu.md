# init(size:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new pixel buffer with a size that you specify.

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
init(size: vImage.Size, pixelFormat: Format.Type = Format.self)
```

Available when `Format` conforms to `StaticPixelFormat`.

#### Discussion

This initializer allocates but doesn’t initialize the pixel buffer’s memory. That is, the operation doesn’t guarantee that all pixel values are zero.

## Parameters

- `size`: The width and height of the buffer.
- `pixelFormat`: The pixel format of the buffer.

## See Also

### Creating a pixel buffer
- [init(size: vImage.Size, pixelFormat: Format.Type)](./init%28size,pixelformat%29-12gl9.md)
  Returns a new multiplane pixel buffer with a size that you specify.
- [init(width: Int, height: Int, pixelFormat: Format.Type)](./init%28width,height,pixelformat%29.md)
  Returns a new pixel buffer with a width and height that you specify.
- [vImage.Size](../size.md)
  A structure that contains width and height values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(size:pixelformat:)-96ocu)*