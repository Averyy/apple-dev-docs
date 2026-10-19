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

The following code shows how to convert an RGB image that’s represented as three planar buffers to grayscale. The call to [`vImageMultiDimensionalInterpolatedLookupTable_PlanarF(_:_:_:_:_:_:)`](vimagemultidimensionalinterpolatedlookuptable_planarf(_:_:_:_:_:_:).md) uses the lookup table from the example code in the Discussion section for  [`vImageMultidimensionalTable_Create(_:_:_:_:_:_:_:)`](vimagemultidimensionaltable_create(_:_:_:_:_:_:_:).md). The source image contains three pixels: One is pure red, one is pure green, and one is pure blue. On return, the destination image contains three pixels with the values `[0.2125887, 0.71519035, 0.072190434]`:

**Swift**:

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

// Prints "[0.21259, 0.71519, 0.07219]".
print(destination.array)
```

**Objective-C**:

```objc
// Build the same 32-entries-per-channel RGB-to-grayscale lookup table
// as the companion vImageMultidimensionalTable_Create example, using
// Rec. 709 coefficients. Samples in [0..65535] map to [0.0, 1.0].
const uint8_t entriesPerChannel = 32;
const uint32_t srcChannelCount = 3;
const uint32_t destChannelCount = 1;

const vImagePixelCount lookupTableElementCount =
    (vImagePixelCount)pow((double)entriesPerChannel,
                          (double)srcChannelCount) * destChannelCount;

uint16_t *tableData = malloc(lookupTableElementCount * sizeof(uint16_t));

const float multiplier = (float)UINT16_MAX;
vImagePixelCount bufferIndex = 0;
for (uint8_t red = 0; red < entriesPerChannel; red++) {
    for (uint8_t green = 0; green < entriesPerChannel; green++) {
        for (uint8_t blue = 0; blue < entriesPerChannel; blue++) {
            float normalizedRed   = (float)red   / (float)(entriesPerChannel - 1);
            float normalizedGreen = (float)green / (float)(entriesPerChannel - 1);
            float normalizedBlue  = (float)blue  / (float)(entriesPerChannel - 1);

            float gray = (normalizedRed   * 0.2126f) +
                         (normalizedGreen * 0.7152f) +
                         (normalizedBlue  * 0.0722f);

            tableData[bufferIndex] = (uint16_t)(gray * multiplier);
            bufferIndex++;
        }
    }
}

const uint8_t entryCountPerSourceChannel[3] = {entriesPerChannel,
                                                entriesPerChannel,
                                                entriesPerChannel};

vImage_Error tableErr = kvImageNoError;
vImage_MultidimensionalTable lookupTable =
    vImageMultidimensionalTable_Create(tableData,
                                      srcChannelCount,
                                      destChannelCount,
                                      entryCountPerSourceChannel,
                                      kvImageMDTableHint_Float,
                                      kvImageNoFlags,
                                      &tableErr);

float redData[3]   = {1, 0, 0};
float greenData[3] = {0, 1, 0};
float blueData[3]  = {0, 0, 1};
float dstData[3]   = {0, 0, 0};

vImage_Buffer redBuf   = { .data = redData,   .width = 1, .height = 3, .rowBytes = 4 };
vImage_Buffer greenBuf = { .data = greenData, .width = 1, .height = 3, .rowBytes = 4 };
vImage_Buffer blueBuf  = { .data = blueData,  .width = 1, .height = 3, .rowBytes = 4 };
vImage_Buffer destBuf  = { .data = dstData,   .width = 1, .height = 3, .rowBytes = 4 };

const vImage_Buffer srcs[3]  = { redBuf, greenBuf, blueBuf };
const vImage_Buffer dests[1] = { destBuf };

vImageMultiDimensionalInterpolatedLookupTable_PlanarF(
    srcs, dests,
    NULL,
    lookupTable,
    kvImageFullInterpolation,
    kvImageNoFlags);

// Prints "[0.21259, 0.71519, 0.07219]".
printf("[%g, %g, %g]\n",
       dstData[0], dstData[1], dstData[2]);

vImageMultidimensionalTable_Release(lookupTable);
free(tableData);
```

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

You can use the same workspace memory for a group of images that are different sizes. To do this, create a vImage buffer structure with a size that shares the maximum width and maximum height of the images that you’re working with. For example, to create a workspace memory that’s suitable for 4x4, 5x4, and 4x5 images, pass a buffer with the size 5x5.

## Parameters

- `srcs`: An array of vImage buffers that reference the source image planes. The number of source buffers is the `numSrcChannels` parameter you pass to [`vImageMultidimensionalTable_Create(_:_:_:_:_:_:_:)`](vimagemultidimensionaltable_create(_:_:_:_:_:_:_:).md).
- `dests`: An array of vImage buffers that reference the destination image planes. The number of destination buffers is the `numDestChannels` parameter you pass to [`vImageMultidimensionalTable_Create(_:_:_:_:_:_:_:)`](vimagemultidimensionaltable_create(_:_:_:_:_:_:_:).md).
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass `nil` to instruct the function to allocate, use, and then free its own temporary buffer.
- `table`: The multidimensional lookup table.
- `method`: The interpolation method, either [`kvImageFullInterpolation`](kvimagefullinterpolation.md) or [`kvImageHalfInterpolation`](kvimagehalfinterpolation.md).
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md). To instruct the function to return the minimum size of the workspace memory, set the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag. Pass [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) to specify that the function returns the minimum temporary buffer size for the operation with the specified parameters.

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