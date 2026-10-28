# encodeTransform(to:sourceTexture:sourceHistogram:sourceHistogramOffset:desiredHistogram:desiredHistogramOffset:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

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
func encodeTransform(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, sourceHistogram: any MTLBuffer, sourceHistogramOffset: Int, desiredHistogram: any MTLBuffer, desiredHistogramOffset: Int)
```

```objc
- (void) encodeTransformToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) source sourceHistogram:(id<MTLBuffer>) sourceHistogram sourceHistogramOffset:(NSUInteger) sourceHistogramOffset desiredHistogram:(id<MTLBuffer>) desiredHistogram desiredHistogramOffset:(NSUInteger) desiredHistogramOffset;
```

## Discussion

The transform function will not begin to execute until after the command buffer has been enqueued and committed. This step will need to be repeated with the new [`MPSKernel`](../mpskernel.md) object if the [`copy(with:device:)`](../mpskernel/copy%28with,device%29.md) or [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md) method is called.

## Parameters

- `commandBuffer`: A valid command buffer.
- `source`: A valid texture containing the source image for the filter.
- `sourceHistogram`: A valid buffer containing the histogram results for the source image. This filter will use these histogram results to generate the cumulative histogram for equalizing the image.  The histogram results per channel are stored together. The number of channels for which histogram results are stored is determined by the number of channels in the image. If the `histogramForAlpha` value of the [`histogramInfo`](./histograminfo.md) property is [`false`](../../Swift/false.md) and the source image is RGBA, then only histogram results for RGB channels are stored.
- `sourceHistogramOffset`: The byte offset into the source histogram buffer where the histogram starts. Must conform to alignment requirements for the `offset` parameter of the [`setBuffer(_:offset:index:)`](../../Metal/mtlcomputecommandencoder/setbuffer%28_,offset,index%29.md) method.
- `desiredHistogram`: A valid buffer containing the desired histogram results for the source image. The histogram results per channel are stored together. The number of channels for which histogram results are stored is determined by the number of channels in the image. If the `histogramForAlpha` value of the [`histogramInfo`](./histograminfo.md) property is [`false`](../../Swift/false.md) and the source image is RGBA, then only histogram results for RGB channels are stored.
- `desiredHistogramOffset`: The byte offset into the desired histogram buffer where the histogram starts. Must conform to alignment requirements for the `offset` parameter of the [`setBuffer(_:offset:index:)`](../../Metal/mtlcomputecommandencoder/setbuffer%28_,offset,index%29.md) method.

## See Also

### Related Documentation
- [func setBufferOffset(Int, index: Int)](../../Metal/mtlcomputecommandencoder/setbufferoffset%28_,index%29.md)
  Changes where the data begins in a buffer already bound to the buffer argument table.
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](../../Metal/mtlcomputecommandencoder/setbuffer%28_,offset,index%29.md)
  Binds a buffer to the buffer argument table, allowing compute kernels to access its data on the GPU.
### Methods
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](./init%28device,histograminfo%29.md)
  Initializes a histogram with specific information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification/encodetransform(to:sourcetexture:sourcehistogram:sourcehistogramoffset:desiredhistogram:desiredhistogramoffset:))*