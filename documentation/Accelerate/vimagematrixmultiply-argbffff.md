# vImageMatrixMultiply_ARGBFFFF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiplies each pixel in an interleaved four-channel, 32-bit source image by a matrix to produce an interleaved four-channel, 32-bit destination image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageMatrixMultiply_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ matrix: UnsafePointer<Float>, _ pre_bias: UnsafePointer<Float>!, _ post_bias: UnsafePointer<Float>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function treats the four-channel source and destination pixels as four-element vectors. The operation multiplies each source pixel by the 4 x 4 matrix to produce the destination pixel.

The following code shows a single-pixel image that contains the ARGB value `(0.1, 0.2, 0.3, 0.4)`. The matrix permutes the channel values to produce a single-pixel destination image that contains the ARGB value `(0.4, 0.3, 0.2, 0.1)`.

```swift
let size = vImage.Size(width: 1, height: 1)

let source = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [0.1, 0.2, 0.3, 0.4],
    size: size)

let destination = vImage.PixelBuffer<vImage.InterleavedFx4>(
    size: size)

let matrix: [Float] = [
    0, 0, 0, 1,
    0, 0, 1, 0,
    0, 1, 0, 0,
    1, 0, 0, 0
]

source.withUnsafePointerToVImageBuffer { src in
    destination.withUnsafePointerToVImageBuffer { dest in
        
        _ = vImageMatrixMultiply_ARGBFFFF(
            src,
            dest,
            matrix,
            nil,
            nil,
            vImage_Flags(kvImageNoFlags))
        
    }
}

// Prints "[0.4, 0.3, 0.2, 0.1]".
print(destination.array)
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `matrix`: An array of values that contains the 4 x 4 matrix elements.
- `pre_bias`: An array that contains four bias values. The function adds the corresponding bias value to each source value before the matrix multiplication step. Pass   to specify zero prebias.
- `post_bias`: An array that contains four bias values. The function adds the corresponding bias value to each destination value after the matrix multiplication step. Pass   to specify zero postbias.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageMatrixMultiply_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Int32, UnsafePointer<Int16>!, UnsafePointer<Int32>!, vImage_Flags) -> vImage_Error](vimagematrixmultiply_argb8888(_:_:_:_:_:_:_:).md)
  Multiplies each pixel in an interleaved four-channel, 8-bit source image by a matrix to produce an interleaved four-channel, 8-bit destination image.
- [func vImageMatrixMultiply_ARGB8888ToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Int32, UnsafePointer<Int16>!, Int32, vImage_Flags) -> vImage_Error](vimagematrixmultiply_argb8888toplanar8(_:_:_:_:_:_:_:).md)
  Multiplies each pixel in an interleaved four-channel, 8-bit source image by a matrix to produce a planar 8-bit destination image.
- [func vImageMatrixMultiply_ARGBFFFFToPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>!, Float, vImage_Flags) -> vImage_Error](vimagematrixmultiply_argbfffftoplanarf(_:_:_:_:_:_:).md)
  Multiplies each pixel in an interleaved four-channel, 32-bit source image by a matrix to produce a planar 32-bit destination image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagematrixmultiply_argbffff(_:_:_:_:_:_:))*