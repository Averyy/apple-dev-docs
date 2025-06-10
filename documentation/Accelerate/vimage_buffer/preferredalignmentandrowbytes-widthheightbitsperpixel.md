# preferredAlignmentAndRowBytes(width:height:bitsPerPixel:)

**Framework**: Accelerate  
**Kind**: method

Returns the preferred alignment and row bytes for a specified size and bits per pixel.

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
static func preferredAlignmentAndRowBytes(width: Int, height: Int, bitsPerPixel: UInt32) throws -> (alignment: Int, rowBytes: Int)
```

#### Return Value

A tuple that contains the alignment and row bytes.

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

- `width`: The width of the image, in pixels.
- `height`: The height of the image, in pixels.
- `bitsPerPixel`: The number of bits in a single pixel.

## See Also

- [init(data: UnsafeMutableRawPointer!, height: vImagePixelCount, width: vImagePixelCount, rowBytes: Int)](vimage_buffer/init(data:height:width:rowbytes:).md)
  Creates a new buffer with the specified size that references existing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/preferredalignmentandrowbytes(width:height:bitsperpixel:))*