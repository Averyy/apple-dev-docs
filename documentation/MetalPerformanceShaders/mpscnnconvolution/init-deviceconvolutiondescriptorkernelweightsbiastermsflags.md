# init(device:convolutionDescriptor:kernelWeights:biasTerms:flags:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a convolution kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)
```

#### Return Value

A valid [`MPSCNNConvolution`](mpscnnconvolution.md) object or `nil`, if failure.

## Parameters

- `device`: The device on which this kernel will run.
- `convolutionDescriptor`: A pointer to a valid convolution descriptor.
- `kernelWeights`: A pointer to a weights array. Each entry is a float value. The number of entries is equal to [`inputFeatureChannels`](mpscnnconvolutiondescriptor/inputfeaturechannels.md) `*` [`outputFeatureChannels`](mpscnnconvolutiondescriptor/outputfeaturechannels.md) `*` [`kernelHeight`](mpscnnconvolutiondescriptor/kernelheight.md) `*` [`kernelWidth`](mpscnnconvolutiondescriptor/kernelwidth.md). The layout of the filter weight is arranged so that it can be reinterpreted as a 4D tensor (array) `weight[outputChannels][kernelHeight][kernelWidth][inputChannels/groups]` Weights are converted to half float precision (`fp16`) internally for best performance.
- `biasTerms`: A pointer to bias terms to be applied to the convolution output. Each entry is a float value. The number of entries is the number of output feature maps.
- `flags`: Currently unused. This value must be [`MPSCNNConvolutionFlags.none`](mpscnnconvolutionflags/none.md).

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnconvolution/init(coder:device:).md)
- [class MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [enum MPSCNNConvolutionFlags](mpscnnconvolutionflags.md)
  Options used to control how kernel weights are stored and used in the CNN kernels
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolution/init(device:weights:).md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/init(device:convolutiondescriptor:kernelweights:biasterms:flags:))*