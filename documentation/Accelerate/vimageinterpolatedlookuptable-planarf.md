# vImageInterpolatedLookupTable_PlanarF(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Uses an interpolated lookup table to transform a 32-bit planar image.

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
func vImageInterpolatedLookupTable_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ table: UnsafePointer<Pixel_F>, _ tableEntries: vImagePixelCount, _ maxFloat: Float, _ minFloat: Float, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Provide this function with a lookup table with any number of values, but with a minimum value of `minFloat` and a maximum value of `maxFloat`. The function generates lookup values by linearly interpolating between the supplied values. The per-pixel conversion calculation is equivalent to the following:

```objc
float clippedPixel = MAX( MIN( src_pixel, maxFloat ), minFloat );    //clip src_pixel to be in range
float fIndex = (float) (tableEntries - 1) * (clippedPixel - minFloat ) / (maxFloat - minFloat);
float fract = fIndex - floor( fIndex );
unsigned long index =  fIndex;
float result = table[ index ] * ( 1.0f - fract ) + table[ index + 1] * fract;
```

The following code shows a lookup table that contains two values, `1` and `0`. The result is that the lookup transformation maps the source values `0...1` to the destination values `1...0`.

```swift
let lookupTable: [Float] = [1, 0]

let source = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.2, 0.4, 0.6, 0.8],
    size: .init(width: 4, height: 1))

let destination = vImage.PixelBuffer<vImage.PlanarF>(
    size: source.size)

source.withUnsafePointerToVImageBuffer{ src in
    destination.withUnsafePointerToVImageBuffer { dest in
        
        _ = vImageInterpolatedLookupTable_PlanarF(
            src,
            dest,
            lookupTable,
            vImagePixelCount(lookupTable.count),
            1, 0,
            vImage_Flags(kvImageNoFlags))
    }
}

// Prints "[0.8, 0.6, 0.4, 0.2]".
print(destination.array)
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `table`: A lookup table that contains   values.
- `tableEntries`: The number of values in the lookup table.
- `maxFloat`: A value of type  .
- `minFloat`: A value of type  .
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  .

## See Also

- [func vImageTableLookUp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](vimagetablelookup_planar8(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to an 8-bit planar image.
- [func vImageLookupTable_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](vimagelookuptable_planarftoplanar8(_:_:_:_:).md)
  Uses a lookup table to transform a 32-bit planar image to an 8-bit planar image.
- [func vImageLookupTable_Planar8toPlanar16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar16(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to an unsigned 16-bit planar image.
- [func vImageLookupTable_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_F>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanarf(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit planar image.
- [func vImageLookupTable_8to64U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt64>, vImage_Flags) -> vImage_Error](vimagelookuptable_8to64u(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 64-bit planar image.
- [func vImageLookupTable_Planar16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar16(_:_:_:_:).md)
  Uses a lookup table to transform a 16-bit planar image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageinterpolatedlookuptable_planarf(_:_:_:_:_:_:_:))*