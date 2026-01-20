# update(with:sourceState:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
optional func update(with gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool
```

## See Also

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
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](mpscnnconvolutiondatasource/weightslayout.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](mpscnnconvolutiondatasource/weightsquantizationtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource/update(with:sourcestate:))*