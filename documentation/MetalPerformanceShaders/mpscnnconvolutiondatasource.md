# MPSCNNConvolutionDataSource

**Framework**: Metal Performance Shaders  
**Kind**: protocol  
**Role**: Protocol

The protocol that provides convolution filter weights and bias terms.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol MPSCNNConvolutionDataSource : NSCopying, NSObjectProtocol
```

```objc
@protocol MPSCNNConvolutionDataSource <NSCopying, NSObject>
```

## Topics

### Instance Methods
- [func biasTerms() -> UnsafeMutablePointer<Float>?](./mpscnnconvolutiondatasource/biasterms%28%29.md)
- [func dataType() -> MPSDataType](./mpscnnconvolutiondatasource/datatype%28%29.md)
- [func descriptor() -> MPSCNNConvolutionDescriptor](./mpscnnconvolutiondatasource/descriptor%28%29.md)
- [func label() -> String?](./mpscnnconvolutiondatasource/label%28%29.md)
- [func load() -> Bool](./mpscnnconvolutiondatasource/load%28%29.md)
- [func lookupTableForUInt8Kernel() -> UnsafeMutablePointer<Float>](./mpscnnconvolutiondatasource/lookuptableforuint8kernel%28%29.md)
- [func purge()](./mpscnnconvolutiondatasource/purge%28%29.md)
- [func rangesForUInt8Kernel() -> UnsafeMutablePointer<vector_float2>](./mpscnnconvolutiondatasource/rangesforuint8kernel%28%29.md)
- [func weights() -> UnsafeMutableRawPointer](./mpscnnconvolutiondatasource/weights%28%29.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpscnnconvolutiondatasource/copy%28with,device%29.md)
- [func kernelWeightsDataType() -> MPSDataType](./mpscnnconvolutiondatasource/kernelweightsdatatype%28%29.md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](./mpscnnconvolutiondatasource/update%28with,gradientstate,sourcestate%29.md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](./mpscnnconvolutiondatasource/update%28with,sourcestate%29.md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](./mpscnnconvolutiondatasource/weightslayout%28%29.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](./mpscnnconvolutiondatasource/weightsquantizationtype%28%29.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnbinaryconvolution/init%28coder,device%29.md)
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryconvolution/init%28device,convolutiondata,outputbiasterms,outputscaleterms,inputbiasterms,inputscaleterms,type,flags%29.md)
  Initializes a binary convolution kernel.
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryconvolution/init%28device,convolutiondata,scalevalue,type,flags%29.md)
  Initializes a binary convolution kernel.
- [enum MPSCNNBinaryConvolutionType](./mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.
- [enum MPSCNNBinaryConvolutionFlags](./mpscnnbinaryconvolutionflags.md)
  Options used to control binary convolution kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource)*