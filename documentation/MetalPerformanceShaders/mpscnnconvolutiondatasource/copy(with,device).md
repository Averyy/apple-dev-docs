# copy(with:device:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
optional func copy(with zone: NSZone? = nil, device: (any MTLDevice)?) -> Self
```

```objc
- (instancetype) copyWithZone:(NSZone *) zone device:(id<MTLDevice>) device;
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
- [func kernelWeightsDataType() -> MPSDataType](./kernelweightsdatatype%28%29.md)
- [func update(with: any MTLCommandBuffer, gradientState: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> MPSCNNConvolutionWeightsAndBiasesState?](./update%28with,gradientstate,sourcestate%29.md)
- [func update(with: MPSCNNConvolutionGradientState, sourceState: MPSCNNConvolutionWeightsAndBiasesState) -> Bool](./update%28with,sourcestate%29.md)
- [func weightsLayout() -> MPSCNNConvolutionWeightsLayout](./weightslayout%28%29.md)
- [func weightsQuantizationType() -> MPSCNNWeightsQuantizationType](./weightsquantizationtype%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondatasource/copy(with:device:))*