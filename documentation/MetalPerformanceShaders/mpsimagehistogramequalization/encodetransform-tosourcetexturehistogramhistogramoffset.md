# encodeTransform(to:sourceTexture:histogram:histogramOffset:)

**Framework**: Metal Performance Shaders  
**Kind**: method

Encodes the transform function to a command buffer using a compute command encoder. The transform function computes the equalization lookup table.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encodeTransform(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)
```

#### Discussion

The transform function will not begin to execute until after the command buffer has been enqueued and committed. This step will need to be repeated with the new [`MPSKernel`](mpskernel.md) object if the [`copy(with:device:)`](mpskernel/copy(with:device:).md) or [`copy(with:)`](https://developer.apple.com/documentation/Foundation/NSCopying/copy(with:)) method is called. The transform is stored as internal state to the object. You still need to call the [`encode(commandBuffer:sourceTexture:destinationTexture:)`](mpsunaryimagekernel/encode(commandbuffer:sourcetexture:destinationtexture:).md) afterward to apply the transform to produce a result texture.

## Parameters

- `commandBuffer`: A valid command buffer.
- `source`: A valid texture containing the source image for the filter.
- `histogram`: A valid buffer containing the histogram results for an image. This filter will use these histogram results to generate the cumulative histogram for equalizing the image. The histogram results per channel are stored together. The number of channels for which histogram results are stored is determined by the number of channels in the image. If the   value of the   property is   and the source image is RGBA, then only histogram results for RGB channels are stored.
- `histogramOffset`: The byte offset into the histogram buffer where the histogram starts. Must conform to alignment requirements for the   parameter of the   method.

## See Also

- [func setBufferOffset(Int, index: Int)](../Metal/MTLComputeCommandEncoder/setBufferOffset(_:index:).md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](../Metal/MTLComputeCommandEncoder/setBuffer(_:offset:index:).md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagehistogramequalization/init(device:histograminfo:).md)
  Initializes a histogram with specific information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization/encodetransform(to:sourcetexture:histogram:histogramoffset:))*