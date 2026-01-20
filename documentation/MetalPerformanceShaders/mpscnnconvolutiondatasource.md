# MPSCNNConvolutionDataSource

**Framework**: Metal Performance Shaders  
**Kind**: protocol

The protocol that provides convolution filter weights and bias terms.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol MPSCNNConvolutionDataSource : NSCopying, NSObjectProtocol
```

## Topics

### Instance Methods
- [func biasTerms() -> UnsafeMutablePointer<Float>?](mpscnnconvolutiondatasource/biasterms.md)
- [func dataType() -> MPSDataType](mpscnnconvolutiondatasource/datatype.md)
- [func descriptor() -> MPSCNNConvolutionDescriptor](mpscnnconvolutiondatasource/descriptor.md)
- [func label() -> String?](mpscnnconvolutiondatasource/label.md)
- [func load() -> Bool](mpscnnconvolutiondatasource/load.md)
- [func lookupTableForUInt8Kernel() -> UnsafeMutablePointer<Float>](mpscnnconvolutiondatasource/lookuptableforuint8kernel.md)
- [func purge()](mpscnnconvolutiondatasource/purge.md)
- [func rangesForUInt8Kernel() -> UnsafeMutablePointer<vector_float2>](mpscnnconvolutiondatasource/rangesforuint8kernel.md)
- [func weights() -> UnsafeMutableRawPointer](mpscnnconvolutiondatasource/weights.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnnconvolutiondatasource/copy(with:device:).md)
- [func kernelWeightsDataType() -> MPSDataType](mpscnnconvolutiondatasource/kernelweightsdatatype.md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](mpscnnconvolutiondatasource/update(with:gradientstate:sourcestate:).md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](mpscnnconvolutiondatasource/update(with:sourcestate:).md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](mpscnnconvolutiondatasource/weightslayout.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](mpscnnconvolutiondatasource/weightsquantizationtype.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbinaryconvolution/init(coder:device:).md)
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/init(device:convolutiondata:outputbiasterms:outputscaleterms:inputbiasterms:inputscaleterms:type:flags:).md)
  Initializes a binary convolution kernel.
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/init(device:convolutiondata:scalevalue:type:flags:).md)
  Initializes a binary convolution kernel.
- [enum MPSCNNBinaryConvolutionType](mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.
- [enum MPSCNNBinaryConvolutionFlags](mpscnnbinaryconvolutionflags.md)
  Options used to control binary convolution kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource)*