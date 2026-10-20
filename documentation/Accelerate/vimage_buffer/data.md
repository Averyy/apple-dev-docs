# data

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A pointer to the top-left pixel of the image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var data: UnsafeMutableRawPointer!
```

```c
void * data;
```

## See Also

### Inspecting a buffer’s properties
- [var height: vImagePixelCount](./height.md)
  The height of the image, in pixels.
- [var width: vImagePixelCount](./width.md)
  The width of the image, in pixels.
- [var size: CGSize](./size.md)
  The size of the image, in pixels.
- [var rowBytes: Int](./rowbytes.md)
  The distance, in bytes, between the start of one pixel row and the next in an image, including any unused space between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/data)*