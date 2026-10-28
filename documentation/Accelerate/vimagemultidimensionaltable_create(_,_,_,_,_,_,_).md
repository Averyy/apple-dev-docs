# vImageMultidimensionalTable_Create(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Creates a multidimensional lookup table.

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
func vImageMultidimensionalTable_Create(_ tableData: UnsafePointer<UInt16>, _ numSrcChannels: UInt32, _ numDestChannels: UInt32, _ table_entries_per_dimension: UnsafePointer<UInt8>, _ hint: vImageMDTableUsageHint, _ flags: vImage_Flags, _ err: UnsafeMutablePointer<vImage_Error>!) -> vImage_MultidimensionalTable!
```

```c
vImage_MultidimensionalTablevImageMultidimensionalTable_Create(const uint16_t *tableData, uint32_t numSrcChannels, uint32_t numDestChannels, const uint8_t table_entries_per_dimension[], vImageMDTableUsageHint hint, vImage_Flags flags, vImage_Error *err);
```

## Mentions

- [Applying color transforms to images with a multidimensional lookup table](./applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

Use a multidimensional lookup table to transform the colors in an image. The lookup table defines an output color based on the input color values. The vImage multidimensional lookup table provides interpolation to compute output color values that don’t have an explicit entry in the table for a specified input color.

A [`vImage_MultidimensionalTable`](./vimage_multidimensionaltable.md) applies transforms to 32-bit and 16Q12 planar pixel buffers.

The following is an example of a simple lookup table that implements the Rec. 709 luminance coefficients to convert from a three-channel RGB image to a single-channel grayscale image. The lookup table is a 3D cube with 32 entries per channel. Supply the lookup values as a contiguous array of samples that defines the lookup table values. The samples have range `0...65535` that the vImage library interprets as the floating-point range `0...1`.

**Swift**:

```swift
let entriesPerChannel = UInt8(32)
let srcChannelCount = 3
let destChannelCount = 1

let lookupTableElementCount = Int(pow(Float(entriesPerChannel),
                                      Float(srcChannelCount))) * Int(destChannelCount)

let tableData = [UInt16](unsafeUninitializedCapacity: lookupTableElementCount) {
    buffer, count in
    
    let multiplier = Float(UInt16.max)
    var bufferIndex = 0
    
    for red in ( 0 ..< entriesPerChannel) {
        for green in ( 0 ..< entriesPerChannel) {
            for blue in ( 0 ..< entriesPerChannel) {
                
                let normalizedRed = Float(red) / Float(entriesPerChannel - 1)
                let normalizedGreen = Float(green) / Float(entriesPerChannel - 1)
                let normalizedBlue = Float(blue) / Float(entriesPerChannel - 1)
                
                let gray = (normalizedRed * 0.2126) +
                           (normalizedGreen * 0.7152) +
                           (normalizedBlue * 0.0722)
                
                buffer[ bufferIndex ] = UInt16(gray * multiplier)
                bufferIndex += 1
            }
        }
    }
    
    count = lookupTableElementCount
}

let entryCountPerSourceChannel = [UInt8](repeating: entriesPerChannel,
                                         count: srcChannelCount)

var error = kvImageNoError

guard let lookupTable = vImageMultidimensionalTable_Create(
        tableData,
        UInt32(srcChannelCount),
        UInt32(destChannelCount),
        entryCountPerSourceChannel,
        kvImageMDTableHint_Float,
        vImage_Flags(kvImageNoFlags),
        &error) else {
    fatalError("Unable to create multidimensional table \(error).")
}

defer {
    vImageMultidimensionalTable_Release(lookupTable)
} 
```

**Objective-C**:

```objc
const uint8_t entriesPerChannel = 32;
const uint32_t srcChannelCount = 3;
const uint32_t destChannelCount = 1;

const vImagePixelCount lookupTableElementCount =
    (vImagePixelCount)pow((double)entriesPerChannel, (double)srcChannelCount) * destChannelCount;

uint16_t *tableData = (uint16_t *)malloc(lookupTableElementCount * sizeof(uint16_t));

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

vImage_Error error = kvImageNoError;

vImage_MultidimensionalTable lookupTable =
    vImageMultidimensionalTable_Create(tableData,
                                       srcChannelCount,
                                       destChannelCount,
                                       entryCountPerSourceChannel,
                                       kvImageMDTableHint_Float,
                                       kvImageNoFlags,
                                       &error);

vImageMultidimensionalTable_Release(lookupTable);
free(tableData);
```

## Parameters

- `tableData`: A pointer to the lookup table data.
- `numSrcChannels`: The number of channels in an input pixel.
- `numDestChannels`: The number of channels in an output pixel.
- `table_entries_per_dimension`: An array that contains the number of table entries for each channel in an input pixel.
- `hint`: A constant that specifies whether this function sets up the table for particular transform functions. If you only use [`vImageMultiDimensionalInterpolatedLookupTable_PlanarF(_:_:_:_:_:_:)`](./vimagemultidimensionalinterpolatedlookuptable_planarf%28_,_,_,_,_,_%29.md), pass [`kvImageMDTableHint_Float`](./kvimagemdtablehint_float.md). If you only use [`vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12(_:_:_:_:_:_:)`](./vimagemultidimensionalinterpolatedlookuptable_planar16q12%28_,_,_,_,_,_%29.md), pass [`kvImageMDTableHint_16Q12`](./kvimagemdtablehint_16q12.md). Pass both flags if you use both transform functions.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).
- `err`: On output, [`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## See Also

### Transforming with a multidimensional lookup table
- [Applying color transforms to images with a multidimensional lookup table](./applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
  Precompute translation values to optimize color space conversion and other pointwise operations.
- [Cropping to the subject in a chroma-keyed image](./cropping-to-the-subject-in-a-chroma-keyed-image.md)
  Convert a chroma-key color to alpha values and trim transparent pixels using Accelerate.
- [Applying transformations to selected colors in an image](./applying-transformations-to-selected-colors-in-an-image.md)
  Desaturate a range of colors in an image with a multidimensional lookup table.
- [func vImageMultiDimensionalInterpolatedLookupTable_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error](./vimagemultidimensionalinterpolatedlookuptable_planarf%28_,_,_,_,_,_%29.md)
  Uses a multidimensional lookup table to transform a 32-bit planar image.
- [func vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error](./vimagemultidimensionalinterpolatedlookuptable_planar16q12%28_,_,_,_,_,_%29.md)
  Uses a multidimensional lookup table to transform a 16Q12 planar image.
- [func vImageMultidimensionalTable_Retain(vImage_MultidimensionalTable!) -> vImage_Error](./vimagemultidimensionaltable_retain%28_%29.md)
  Retains a multidimensional table.
- [func vImageMultidimensionalTable_Release(vImage_MultidimensionalTable!) -> vImage_Error](./vimagemultidimensionaltable_release%28_%29.md)
  Releases a multidimensional table.
- [typealias vImage_MultidimensionalTable](./vimage_multidimensionaltable.md)
  An opaque pointer that represents a multidimensional lookup table.
- [struct vImageMDTableUsageHint](./vimagemdtableusagehint.md)
  Constants that indicate the use for a multidimensional lookup table.
- [struct vImage_InterpolationMethod](./vimage_interpolationmethod.md)
  Constants that represent different interpolation methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagemultidimensionaltable_create(_:_:_:_:_:_:_:))*