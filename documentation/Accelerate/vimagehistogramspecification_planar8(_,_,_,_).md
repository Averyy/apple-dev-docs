# vImageHistogramSpecification_Planar8(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Specifies the histogram of an 8-bit planar buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageHistogramSpecification_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ desired_histogram: UnsafePointer<vImagePixelCount>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageHistogramSpecification_Planar8(const vImage_Buffer *src, const vImage_Buffer *dest, const vImagePixelCount *desired_histogram, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

Use this function to apply a histogram — that you’ve generated using [`vImageHistogramCalculation_Planar8(_:_:_:)`](./vimagehistogramcalculation_planar8%28_,_,_%29.md) — to another image.

The following code applies a histogram to a planar vImage buffer:

**Swift**:

```swift
let source = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [10, 20, 30, 40],
    size: .init(width: 4, height: 1))

var histogram = [vImagePixelCount](repeating: 0, count: 256)
histogram[64]  = 1
histogram[128] = 1
histogram[192] = 1
histogram[255] = 1

let destination = vImage.PixelBuffer<vImage.Planar8>(
    size: .init(width: 4, height: 1))

source.withUnsafePointerToVImageBuffer { src in
    destination.withUnsafePointerToVImageBuffer { dest in
        histogram.withUnsafeBufferPointer { histPtr in
            _ = vImageHistogramSpecification_Planar8(src,
                                                     dest,
                                                     histPtr.baseAddress!,
                                                     vImage_Flags(kvImageNoFlags))
        }
    }
}

// Prints "[64, 128, 192, 255]".
print(destination.array)
```

**Objective-C**:

```objc
// The `histogram` is a 256-element array.
// The `buffer` is a `vImage_Buffer` structure.
vImageHistogramSpecification_Planar8(&buffer, &buffer,
                                     histogram,
                                     kvImageNoFlags);
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `desired_histogram`: The histogram that the operation applies to the source buffer.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Related Documentation
- [Enhancing image contrast with histogram manipulation](./enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Specifying histograms with vImage](./specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
### Specifying a histogram
- [func vImageHistogramSpecification_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](./vimagehistogramspecification_planarf%28_,_,_,_,_,_,_,_%29.md)
  Specifies the histogram of a 32-bit planar buffer.
- [func vImageHistogramSpecification_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](./vimagehistogramspecification_argb8888%28_,_,_,_%29.md)
  Specifies the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageHistogramSpecification_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](./vimagehistogramspecification_argbffff%28_,_,_,_,_,_,_,_%29.md)
  Specifes the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehistogramspecification_planar8(_:_:_:_:))*