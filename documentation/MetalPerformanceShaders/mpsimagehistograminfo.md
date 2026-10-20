# MPSImageHistogramInfo

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

The information used to compute the histogram channels of an image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSImageHistogramInfo
```

```c
typedef struct { ... } MPSImageHistogramInfo;
```

## Topics

### Fields
- [var numberOfHistogramEntries: Int](./mpsimagehistograminfo/numberofhistogramentries.md)
  Specifies the number of histogram entries (*bins*) for each channel.
- [var histogramForAlpha: ObjCBool](./mpsimagehistograminfo/histogramforalpha.md)
  Specifies whether the histogram for the alpha channel should be computed or not.
- [var minPixelValue: vector_float4](./mpsimagehistograminfo/minpixelvalue.md)
  Specifies the minimum pixel value. Any pixel value less than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This minimum value is applied to each of the four channels separately.
- [var maxPixelValue: vector_float4](./mpsimagehistograminfo/maxpixelvalue.md)
  Specifies the maximum pixel value.  Any pixel value greater than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This maximum value is applied to each of the four channels separately.
### Initializers
- [init()](./mpsimagehistograminfo/init%28%29.md)
- [init(numberOfHistogramEntries: Int, histogramForAlpha: ObjCBool, minPixelValue: vector_float4, maxPixelValue: vector_float4)](./mpsimagehistograminfo/init%28numberofhistogramentries,histogramforalpha,minpixelvalue,maxpixelvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Methods
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](./mpsimagehistogram/init%28device,histograminfo%29.md)
  Initializes a histogram with specific information.
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](./mpsimagehistogram/encode%28to,sourcetexture,histogram,histogramoffset%29.md)
  Encodes the filter to a command buffer using a compute command encoder.
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](./mpsimagehistogram/histogramsize%28forsourceformat%29.md)
  The amount of space the histogram will take up in the output buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo)*