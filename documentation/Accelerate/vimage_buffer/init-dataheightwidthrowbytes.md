# init(data:height:width:rowBytes:)

**Framework**: Accelerate  
**Kind**: init

Creates a new buffer with the specified size that references existing data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(data: UnsafeMutableRawPointer!, height: vImagePixelCount, width: vImagePixelCount, rowBytes: Int)
```

#### Discussion

If you provide your own buffer storage, call [`preferredAlignmentAndRowBytes(width:height:bitsPerPixel:)`](vimage_buffer/preferredalignmentandrowbytes(width:height:bitsperpixel:).md) to get the row stride that ensures your buffer achieves the best performance.

```swift
let width = 10
let height = 5

let alignmentAndRowBytes = try vImage_Buffer.preferredAlignmentAndRowBytes(
    width: width,
    height: height,
    bitsPerPixel: 8)

// Prints "16".
print(alignmentAndRowBytes.rowBytes)

let data = UnsafeMutableRawPointer.allocate(
    byteCount: alignmentAndRowBytes.rowBytes * height,
    alignment: alignmentAndRowBytes.alignment)

let buffer = vImage_Buffer(data: data,
                           height: vImagePixelCount(height),
                           width: vImagePixelCount(width),
                           rowBytes: alignmentAndRowBytes.rowBytes)
```

## Parameters

- `data`: A pointer to the top-left pixel of the buffer.
- `height`: The height of the buffer, in pixels.
- `width`: The width of the buffer, in pixels.
- `rowBytes`: The number of bytes in a pixel row.

## See Also

- [static func preferredAlignmentAndRowBytes(width: Int, height: Int, bitsPerPixel: UInt32) throws -> (alignment: Int, rowBytes: Int)](vimage_buffer/preferredalignmentandrowbytes(width:height:bitsperpixel:).md)
  Returns the preferred alignment and row bytes for a specified size and bits per pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/init(data:height:width:rowbytes:))*