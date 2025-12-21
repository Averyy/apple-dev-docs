# vImageMultiDimensionalInterpolatedLookupTable_PlanarF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Uses a multidimensional lookup table to transform a 32-bit planar image.

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
func vImageMultiDimensionalInterpolatedLookupTable_PlanarF(_ srcs: UnsafePointer<vImage_Buffer>, _ dests: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ table: vImage_MultidimensionalTable, _ method: vImage_InterpolationMethod, _ flags: vImage_Flags) -> vImage_Error
```

## Mentions

- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

The following code shows how to convert an RGB image that’s represented as three planar buffers to grayscale. The call to [`vImageMultiDimensionalInterpolatedLookupTable_PlanarF(_:_:_:_:_:_:)`](vimagemultidimensionalinterpolatedlookuptable_planarf(_:_:_:_:_:_:).md) uses the lookup table from the example code in the Discussion section for  [`vImageMultidimensionalTable_Create(_:_:_:_:_:_:_:)`](vimagemultidimensionaltable_create(_:_:_:_:_:_:_:).md). The source image contains three pixels, one is pure red, one is pure green, and one is pure blue. On return, the destination image contains three pixels with the values `[0.2125887, 0.71519035, 0.072190434]`.

```swift
let size = vImage.Size(width: 1, height: 3)

let red = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [1, 0, 0],
    size: size)
let green = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0, 1, 0],
    size: size)
let blue = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0, 0, 1],
    size: size)

let source = vImage.PixelBuffer<vImage.PlanarFx3>(
    planarBuffers: [red, green, blue])

let destination = vImage.PixelBuffer<vImage.PlanarF>(
    size: size)

source.withUnsafeVImageBuffers { src in
    destination.withUnsafeVImageBuffer { dest in
        
        _ = vImageMultiDimensionalInterpolatedLookupTable_PlanarF(
            src,
            [dest],
            nil,
            lookupTable,
            kvImageFullInterpolation,
            vImage_Flags(kvImageNoFlags))
    }
}

// Prints "[0.2125887, 0.71519035, 0.072190434]".
print(destination.array)
```

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `srcs`: An array of vImage buffers that reference the source image planes. The number of source buffers is the   parameter you pass to  .
- `dests`: An array of vImage buffers that reference the destination image planes. The number of destination buffers is the   parameter you pass to  .
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `table`: The multidimensional lookup table.
- `method`: The interpolation method, either   or  .
- `flags`: Pass   to specify that the function returns the minimum temporary buffer size for the operation with the specified parameters.

## See Also

- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
  Precompute translation values to optimize color space conversion and other pointwise operations.
- [Cropping to the subject in a chroma-keyed image](cropping-to-the-subject-in-a-chroma-keyed-image.md)
  Convert a chroma-key color to alpha values and trim transparent pixels using Accelerate.
- [Applying transformations to selected colors in an image](applying-transformations-to-selected-colors-in-an-image.md)
  Desaturate a range of colors in an image with a multidimensional lookup table.
- [func vImageMultidimensionalTable_Create(UnsafePointer<UInt16>, UInt32, UInt32, UnsafePointer<UInt8>, vImageMDTableUsageHint, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> vImage_MultidimensionalTable!](vimagemultidimensionaltable_create(_:_:_:_:_:_:_:).md)
  Creates a multidimensional lookup table.
- [func vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error](vimagemultidimensionalinterpolatedlookuptable_planar16q12(_:_:_:_:_:_:).md)
  Uses a multidimensional lookup table to transform a 16Q12 planar image.
- [func vImageMultidimensionalTable_Retain(vImage_MultidimensionalTable!) -> vImage_Error](vimagemultidimensionaltable_retain(_:).md)
  Retains a multidimensional table.
- [func vImageMultidimensionalTable_Release(vImage_MultidimensionalTable!) -> vImage_Error](vimagemultidimensionaltable_release(_:).md)
  Releases a multidimensional table.
- [typealias vImage_MultidimensionalTable](vimage_multidimensionaltable.md)
  An opaque pointer that represents a multidimensional lookup table.
- [struct vImageMDTableUsageHint](vimagemdtableusagehint.md)
  Constants that indicate the use for a multidimensional lookup table.
- [struct vImage_InterpolationMethod](vimage_interpolationmethod.md)
  Constants that represent different interpolation methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagemultidimensionalinterpolatedlookuptable_planarf(_:_:_:_:_:_:))*