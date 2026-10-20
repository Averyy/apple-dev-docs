# weights()

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func weights() -> UnsafeMutableRawPointer
```

```objc
- (void *) weights;
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
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./copy%28with,device%29.md)
- [func kernelWeightsDataType() -> MPSDataType](./kernelweightsdatatype%28%29.md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](./update%28with,gradientstate,sourcestate%29.md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](./update%28with,sourcestate%29.md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](./weightslayout%28%29.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](./weightsquantizationtype%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource/weights())*