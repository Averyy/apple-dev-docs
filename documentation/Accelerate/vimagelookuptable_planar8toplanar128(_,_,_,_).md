# vImageLookupTable_Planar8toPlanar128(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, four-channel interleaved image.

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
func vImageLookupTable_Planar8toPlanar128(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ table: UnsafePointer<Pixel_FFFF>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageLookupTable_Planar8toPlanar128(const vImage_Buffer *src, const vImage_Buffer *dest, const Pixel_FFFF table[256], vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

For each pixel, this function uses the 8-bit value from the source image as an index to the [`Pixel_FFFF`](./pixel_ffff.md) value from the table. The per-pixel conversion calculation is equivalent to the following:

```c
uint32_t table[256*4];       // 128 bits per pixel and 32 bits per channel.
uint32_t *t_ptr = (uint32_t*)(table + 4 * srcRow[i]);
uint32_t a = t_ptr[0];
uint32_t r = t_ptr[1];
uint32_t g = t_ptr[2];
uint32_t b = t_ptr[3];
dstRow[3*i+0] = a;
dstRow[3*i+1] = r;
dstRow[3*i+2] = g;
dstRow[3*i+3] = b;
```

The following code shows how to create a lookup table that maps all source pixel values to a constant RGB value of `(10, 20, 30)`:

**Swift**:

```swift
let alpha: Pixel_F = 10
let red: Pixel_F = 20
let green: Pixel_F = 30
let blue: Pixel_F = 40
let lookupValue = Pixel_FFFF(alpha, red, green, blue)

let lookupTable = [Pixel_FFFF](repeating: lookupValue, count: 256)

let source = vImage.PixelBuffer<vImage.Planar8>(
    size: .init(width: 3, height: 1))
let destination = vImage.PixelBuffer<vImage.InterleavedFx4>(
    size: .init(width: 3, height: 1))

source.withUnsafePointerToVImageBuffer{ src in
    destination.withUnsafePointerToVImageBuffer { dest in
        
        _ = vImageLookupTable_Planar8toPlanar128(
            src,
            dest,
            lookupTable,
            vImage_Flags(kvImageNoFlags))
        
    }
}

// Prints "[10.0, 20.0, 30.0, 40.0,  10.0, 20.0, 30.0, 40.0,  10.0, 20.0, 30.0, 40.0]".
print(destination.array)
```

**Objective-C**:

```objc
float alpha = 10.0f;
float red   = 20.0f;
float green = 30.0f;
float blue  = 40.0f;

Pixel_FFFF lookupTable[256];
for (int i = 0; i < 256; i++) {
    lookupTable[i][0] = alpha;
    lookupTable[i][1] = red;
    lookupTable[i][2] = green;
    lookupTable[i][3] = blue;
}

uint8_t srcData[3] = {0, 1, 2};

vImage_Buffer srcBuf = {
    .data = srcData,
    .width = 3,
    .height = 1,
    .rowBytes = 3
};

float dstData[12] = {0};

vImage_Buffer dstBuf = {
    .data = dstData,
    .width = 3,
    .height = 1,
    .rowBytes = 48
};

vImageLookupTable_Planar8toPlanar128(&srcBuf, &dstBuf,
                                     lookupTable, kvImageNoFlags);

// Prints "[10, 20, 30, 40,  10, 20, 30, 40,  10, 20, 30, 40]".
printf("[%g, %g, %g, %g,  %g, %g, %g, %g,  %g, %g, %g, %g]\n",
       dstData[0], dstData[1], dstData[2], dstData[3],
       dstData[4], dstData[5], dstData[6], dstData[7],
       dstData[8], dstData[9], dstData[10], dstData[11]);
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `table`: A lookup table that contains 256 [`Pixel_FFFF`](./pixel_ffff.md) values.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Transforming planar-to-interleaved with a lookup table
- [func vImageLookupTable_Planar8toPlanar24(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt32>, vImage_Flags) -> vImage_Error](./vimagelookuptable_planar8toplanar24%28_,_,_,_%29.md)
  Uses a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar48(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt64>, vImage_Flags) -> vImage_Error](./vimagelookuptable_planar8toplanar48%28_,_,_,_%29.md)
  Uses a lookup table to transform an 8-bit planar image to a 16-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar96(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_FFFF>, vImage_Flags) -> vImage_Error](./vimagelookuptable_planar8toplanar96%28_,_,_,_%29.md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagelookuptable_planar8toplanar128(_:_:_:_:))*