# size

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The size of the image, in pixels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
var size: CGSize { get }
```

## See Also

### Inspecting a buffer’s properties
- [var data: UnsafeMutableRawPointer!](./data.md)
  A pointer to the top-left pixel of the image.
- [var height: vImagePixelCount](./height.md)
  The height of the image, in pixels.
- [var width: vImagePixelCount](./width.md)
  The width of the image, in pixels.
- [var rowBytes: Int](./rowbytes.md)
  The distance, in bytes, between the start of one pixel row and the next in an image, including any unused space between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/size)*