# vImageByteSwap_Planar16U(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Byte-swaps an unsigned 16-bit planar buffer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageByteSwap_Planar16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Call this function to swap the byte ordering of each pixel in an unsigned 16-bit planar image. Byte-swapping converts the image between big endian and little endian architectures.

The following code converts the two pixels in the pixel buffer from `[”AABB”, “11FF”]` to `[”BBAA”, “FF11”]`:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.Planar16U>(
    pixelValues: [
        UInt16("AABB", radix: 16) ?? 0,
        UInt16("11FF", radix: 16) ?? 0],
    size: .init(width: 2, height: 1))

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    _ = vImageByteSwap_Planar16U(buf,
                                 buf,
                                 vImage_Flags(kvImageNoFlags))
}

// Prints "["bbaa", "ff11"]".
print(pixelBuffer.array.map {String($0, radix: 16)})
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebyteswap_planar16u(_:_:_:))*