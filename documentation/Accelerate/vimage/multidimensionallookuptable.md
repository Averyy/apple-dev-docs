# vImage.MultidimensionalLookupTable

**Framework**: Accelerate  
**Kind**: struct

A multidimensional lookup table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct MultidimensionalLookupTable
```

## Mentions

- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)

#### Overview

Use a multidimensional lookup table to transform the colors in an image. The lookup table defines an output color based on the input color values. The vImage multidimensional lookup table provides interpolation to compute output color values that don’t have an explicit entry in the table for a given input color.

A [`vImage.MultidimensionalLookupTable`](vimage/multidimensionallookuptable.md) applies transforms to 32-bit planar pixel buffers. There are pixel buffer functions available to convert between bit depths and interleaved to planar buffers.

The following is an example of a simple lookup table that implements the Rec. 709 luma coefficients to convert from a 3-channel RGB image to a single-channel grayscale image. The lookup table is a 3D cube with 32 entries per channel.

```swift
let entriesPerChannel = UInt8(32)
let srcChannelCount = 3
let destChannelCount = 1

let lookupTableElementCount = Int(pow(Float(entriesPerChannel),
                                      Float(srcChannelCount))) *
Int(destChannelCount)

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
```

Use the lookup table data to create a [`vImage.MultidimensionalLookupTable`](vimage/multidimensionallookuptable.md) structure.

```swift
let entryCountPerSourceChannel = [UInt8](repeating: entriesPerChannel,
                                         count: srcChannelCount)

let lookupTable = vImage.MultidimensionalLookupTable(
    entryCountPerSourceChannel: entryCountPerSourceChannel,
    destinationChannelCount: destChannelCount,
    data: tableData)
```

Call the `[`apply(sources:destinations:interpolation:)`](vimage/multidimensionallookuptable/apply(sources:destinations:interpolation:).md)` function to transform a 3-channel RGB image to a grayscale image. In this example, the source is interleaved. The code demonstrates calling [`planarBuffers()`](vimage/pixelbuffer/planarbuffers()-462ja.md) to deinterleave the source.

```swift
let src = vImage.PixelBuffer<vImage.InterleavedFx3>( ... )

let planarSources = src.planarBuffers()

let dest = vImage.PixelBuffer<vImage.PlanarF>(size: src.size)

lookupTable.apply(sources: planarSources,
                  destinations: [dest],
                  interpolation: .none)
```

On return, `dest` contains a grayscale representation of the source RGB image.

## Topics

### Initializers
- [init<T>(entryCountPerSourceChannel: [UInt8], destinationChannelCount: Int, data: T)](vimage/multidimensionallookuptable/init(entrycountpersourcechannel:destinationchannelcount:data:).md)
  Returns a new multidimensional lookup table.
### Instance Properties
- [let destinationChannelCount: Int](vimage/multidimensionallookuptable/destinationchannelcount.md)
  The number of destination channels.
- [let entryCountPerSourceChannel: [UInt8]](vimage/multidimensionallookuptable/entrycountpersourcechannel.md)
  An array that contains the number of table entries for each dimension of the lookup table.
- [let sourceChannelCount: Int](vimage/multidimensionallookuptable/sourcechannelcount.md)
  The number of source channels.
### Instance Methods
- [func apply<SrcFormat, DestFormat>(source: vImage.PixelBuffer<SrcFormat>, destination: vImage.PixelBuffer<DestFormat>, interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod)](vimage/multidimensionallookuptable/apply(source:destination:interpolation:).md)
  Transforms a multiple plane pixel buffer using the multidimensional lookup table.
- [func apply(sources: [vImage.PixelBuffer<vImage.PlanarF>], destinations: [vImage.PixelBuffer<vImage.PlanarF>], interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod)](vimage/multidimensionallookuptable/apply(sources:destinations:interpolation:).md)
  Transforms an array of planar pixel buffers using the multidimensional lookup table.
### Enumerations
- [vImage.MultidimensionalLookupTable.InterpolationMethod](vimage/multidimensionallookuptable/interpolationmethod.md)
  Describes the method a multidimensional lookup table uses the generate interpolated values between lookup table values.

## See Also

- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
  Precompute translation values to optimize color space conversion and other pointwise operations.
- [typealias StructuringElement](vimage/structuringelement.md)
  A 2D matrix that represents a morphology kernel.
- [vImage.ConvolutionKernel](vimage/convolutionkernel.md)
  Constants that describe 1D convolution kernels.
- [vImage.ConvolutionKernel2D](vimage/convolutionkernel2d.md)
  A 2D matrix that represents a convolution kernel.
- [vImage.DynamicPixelFormat](vimage/dynamicpixelformat.md)
  A buffer that contains pixels with a data type that’s unknown at compile time.
- [vImage.Interleaved16Fx2](vimage/interleaved16fx2.md)
  A two-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.Interleaved16Fx4](vimage/interleaved16fx4.md)
  A four-channel, 16-bit-per-channel, floating-point interleaved buffer.
- [vImage.Interleaved16Ux2](vimage/interleaved16ux2.md)
  A two-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved16Ux4](vimage/interleaved16ux4.md)
  A four-channel, 16-bit-per-channel, unsigned-integer interleaved buffer.
- [vImage.Interleaved8x2](vimage/interleaved8x2.md)
  A two-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x3](vimage/interleaved8x3.md)
  A three-channel, 8-bit-per-channel interleaved buffer.
- [vImage.Interleaved8x4](vimage/interleaved8x4.md)
  A four-channel, 8-bit-per-channel interleaved buffer.
- [vImage.InterleavedFx2](vimage/interleavedfx2.md)
  A two-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx3](vimage/interleavedfx3.md)
  A three-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.InterleavedFx4](vimage/interleavedfx4.md)
  A four-channel, 32-bit-per-channel, floating-point interleaved buffer.
- [vImage.Options](vimage/options.md)
  Set flags on vImage operations to specify processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/multidimensionallookuptable)*