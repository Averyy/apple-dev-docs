# vImageLookupTable_Planar8toPlanar48(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Uses a lookup table to transform an 8-bit planar image to a 16-bit-per-channel, three-channel interleaved image.

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
func vImageLookupTable_Planar8toPlanar48(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ table: UnsafePointer<UInt64>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageLookupTable_Planar8toPlanar48(const vImage_Buffer *src, const vImage_Buffer *dest, const uint64_t table[256], vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

For each pixel, this function uses the 8-bit value from the source image as an index to the 48-bit value from the table. The per-pixel conversion calculation is equivalent to the following:

```c
uint64_t table[256];       // 64 bits per pixel and 16 bits per channel.
uint16_t *t_ptr = (uint16_t*)(table + srcRow[i]);
uint16_t r = t_ptr[1];
uint16_t g = t_ptr[2];
uint16_t b = t_ptr[3];
dstRow[3*i+0] = r;
dstRow[3*i+1] = g;
dstRow[3*i+2] = b;
```

The following code shows how to create a lookup table that maps all source pixel values to a constant RGB value of `(10, 20, 30)`:

**Swift**:

```swift
let red: Pixel_16F = 10
let green: Pixel_16F = 20
let blue: Pixel_16F = 30
let lookupValue = (UInt64(blue) << 48) | (UInt64(green) << 32) | (UInt64(red) << 16)

let lookupTable = [UInt64](repeating: lookupValue, count: 256)

let source = vImage.PixelBuffer<vImage.Planar8>(
    size: .init(width: 5, height: 1))
let destination = vImage.PixelBuffer<vImage.Planar16F>(
    size: .init(width: 15, height: 1))

source.withUnsafePointerToVImageBuffer { src in
    destination.withUnsafeVImageBuffer { dest in
        
        var intermediate = vImage_Buffer(
            data: dest.data,
            height: dest.height,
            width: 5,
            rowBytes: dest.rowBytes)
        
        _ = vImageLookupTable_Planar8toPlanar48(
            src,
            &intermediate,
            lookupTable,
            vImage_Flags(kvImageNoFlags))
        
    }
}

// Prints "[10, 20, 30,  10, 20, 30,  10, 20, 30,  10, 20, 30,  10, 20, 30]".
print(destination.array)
```

**Objective-C**:

```objc
uint16_t red   = 10;
uint16_t green = 20;
uint16_t blue  = 30;
uint64_t lookupValue = ((uint64_t)blue << 48) | ((uint64_t)green << 32) | ((uint64_t)red << 16);

uint64_t lookupTable[256];
for (int i = 0; i < 256; i++) {
    lookupTable[i] = lookupValue;
}

uint8_t srcData[5] = {0, 1, 2, 3, 4};

vImage_Buffer srcBuf = {
    .data = srcData,
    .width = 5,
    .height = 1,
    .rowBytes = 5
};

uint16_t dstData[15] = {0};

vImage_Buffer dstBuf = {
    .data = dstData,
    .width = 5,
    .height = 1,
    .rowBytes = 30
};

vImageLookupTable_Planar8toPlanar48(&srcBuf, &dstBuf,
                                    lookupTable, kvImageNoFlags);

// Prints "[10, 20, 30,  10, 20, 30,  10, 20, 30,  10, 20, 30,  10, 20, 30]".
printf("[%d, %d, %d,  %d, %d, %d,  %d, %d, %d,  %d, %d, %d,  %d, %d, %d]\n",
       dstData[0], dstData[1], dstData[2],
       dstData[3], dstData[4], dstData[5],
       dstData[6], dstData[7], dstData[8],
       dstData[9], dstData[10], dstData[11],
       dstData[12], dstData[13], dstData[14]);
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `table`: A lookup table that contains 256 [`uint64_t`](../kernel/uint64_t.md) values. The upper 48 bits of each value stores the red, green, and blue values.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Transforming planar-to-interleaved with a lookup table
- [func vImageLookupTable_Planar8toPlanar24(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt32>, vImage_Flags) -> vImage_Error](./vimagelookuptable_planar8toplanar24%28_,_,_,_%29.md)
  Uses a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar96(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_FFFF>, vImage_Flags) -> vImage_Error](./vimagelookuptable_planar8toplanar96%28_,_,_,_%29.md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar128(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_FFFF>, vImage_Flags) -> vImage_Error](./vimagelookuptable_planar8toplanar128%28_,_,_,_%29.md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, four-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagelookuptable_planar8toplanar48(_:_:_:_:))*