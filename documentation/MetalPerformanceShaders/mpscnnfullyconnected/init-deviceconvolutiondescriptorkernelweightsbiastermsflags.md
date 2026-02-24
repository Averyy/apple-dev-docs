# init(device:convolutionDescriptor:kernelWeights:biasTerms:flags:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a fully connected convolution layer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)
```

#### Return Value

A valid [`MPSCNNFullyConnected`](mpscnnfullyconnected.md) object or `nil`, if failure.

#### Discussion

> **Note**:  The encode methods in the [`MPSCNNKernel`](mpscnnkernel.md) class can be used to encode an [`MPSCNNFullyConnected`](mpscnnfullyconnected.md) object to a [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) object.

## Parameters

- `device`: The device on which this kernel will run.
- `convolutionDescriptor`: A valid convolution descriptor. The values of the````MPSCNNConvolutionDescriptor/strideInPixelsX``, ``MPSCNNConvolutionDescriptor/strideInPixelsY``, and ``MPSCNNConvolutionDescriptor/groups`` properties of the descriptor must be set to`1` (i.e. their default values).
- `kernelWeights`: A pointer to a weights array. Each entry is a float value. The number of entries is equal to [`inputFeatureChannels`](mpscnnconvolutiondescriptor/inputfeaturechannels.md) `*` [`outputFeatureChannels`](mpscnnconvolutiondescriptor/outputfeaturechannels.md) `*` [`kernelHeight`](mpscnnconvolutiondescriptor/kernelheight.md) `*` [`kernelWidth`](mpscnnconvolutiondescriptor/kernelwidth.md). The layout of the filter weights is arranged so that it can be reinterpreted as a 4D tensor (array) `weight[outputFeatureChannels][kernelHeight][kernelWidth][inputChannels/groups].` Weights are converted to half float precision (`fp16`) internally for best performance.
- `biasTerms`: A pointer to bias terms to be applied to the convolution output. Each entry is a float value. The number of entries is the number of output feature maps.
- `flags`: Currently unused. This value must be [`MPSCNNConvolutionFlags.none`](mpscnnconvolutionflags/none.md).

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnfullyconnected/init(coder:device:).md)
  Initializes a fully connected convolution layer.
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnfullyconnected/init(device:weights:).md)
  Initializes a fully connected convolution layer.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [class MPSCNNConvolutionDescriptor](mpscnnconvolutiondescriptor.md)
  A description of the attributes of a convolution kernel.
- [enum MPSCNNConvolutionFlags](mpscnnconvolutionflags.md)
  Options used to control how kernel weights are stored and used in the CNN kernels


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnected/init(device:convolutiondescriptor:kernelweights:biasterms:flags:))*