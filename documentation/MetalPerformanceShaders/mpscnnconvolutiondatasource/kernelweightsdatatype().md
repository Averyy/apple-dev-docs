# kernelWeightsDataType()

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func kernelWeightsDataType() -> MPSDataType
```

```objc
- (MPSDataType) kernelWeightsDataType;
```

## See Also

### Instance Methods
- [func biasTerms() -> UnsafeMutablePointer<Float>?](./biasterms%28%29.md)
- [func dataType() -> MPSDataType](./datatype%28%29.md)
- [func descriptor() -> MPSCNNConvolutionDescriptor](./descriptor%28%29.md)
- [func label() -> String?](./label%28%29.md)
- [func load() -> Bool](./load%28%29.md)
- [func lookupTableForUInt8Kernel() -> UnsafeMutablePointer<Float>](./lookuptableforuint8kernel%28%29.md)
- [func purge()](./purge%28%29.md)
- [func rangesForUInt8Kernel() -> UnsafeMutablePointer<vector_float2>](./rangesforuint8kernel%28%29.md)
- [func weights() -> UnsafeMutableRawPointer](./weights%28%29.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./copy%28with,device%29.md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](./update%28with,gradientstate,sourcestate%29.md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](./update%28with,sourcestate%29.md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](./weightslayout%28%29.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](./weightsquantizationtype%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource/kernelweightsdatatype())*