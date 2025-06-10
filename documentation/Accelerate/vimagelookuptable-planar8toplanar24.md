# vImageLookupTable_Planar8toPlanar24(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Uses a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.

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
func vImageLookupTable_Planar8toPlanar24(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ table: UnsafePointer<UInt32>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

For each pixel, this function uses the 8-bit value from the source image as an index to the 24-bit value from the table. The per-pixel conversion calculation is equivalent to the following:

```swift
uint32_t table[256];       // 32 bits per pixel and 8 bits per channel.
uint8_t *t_ptr = (uint8_t*)(table + srcRow[i]);
uint8_t r = t_ptr[1];
uint8_t g = t_ptr[2];
uint8_t b = t_ptr[3];
dstRow[3*i+0] = r;
dstRow[3*i+1] = g;
dstRow[3*i+2] = b;
```

The following code shows how to create a lookup table that maps all source pixel values to a constant RGB value of `(10, 20, 30)`:

```swift
let red: Pixel_8 = 10
let green: Pixel_8 = 20
let blue: Pixel_8 = 30
let lookupValue = (UInt32(blue) << 24) | (UInt32(green) << 16) | (UInt32(red) << 8)

let lookupTable = [UInt32](repeating: lookupValue, count: 256)

let source = vImage.PixelBuffer<vImage.Planar8>(
    size: .init(width: 5, height: 1))
let destination = vImage.PixelBuffer<vImage.Interleaved8x3>(
    size: .init(width: 5, height: 1))

source.withUnsafePointerToVImageBuffer { src in
    destination.withUnsafePointerToVImageBuffer { dest in
        
        _ = vImageLookupTable_Planar8toPlanar24(
            src,
            dest,
            lookupTable,
            vImage_Flags(kvImageNoFlags))
    }
}

// Prints "[10, 20, 30,  10, 20, 30,  10, 20, 30,  10, 20, 30,  10, 20, 30]".
print(destination.array)
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `table`: A lookup table that contains 256   values. The upper 24 bits of each value stores the red, green, and blue values.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageLookupTable_Planar8toPlanar48(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt64>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar48(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 16-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar96(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_FFFF>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar96(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar128(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_FFFF>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar128(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, four-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagelookuptable_planar8toplanar24(_:_:_:_:))*