# init(source:weights:scaleValue:type:flags:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(source sourceNode: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)
```

```objc
- (instancetype) initWithSource:(MPSNNImageNode *) sourceNode weights:(id<MPSCNNConvolutionDataSource>) weights scaleValue:(float) scaleValue type:(MPSCNNBinaryConvolutionType) type flags:(MPSCNNBinaryConvolutionFlags) flags;
```

## See Also

### Initializers
- [protocol MPSCNNConvolutionDataSource](../mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [enum MPSCNNBinaryConvolutionType](../mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.
- [enum MPSCNNBinaryConvolutionFlags](../mpscnnbinaryconvolutionflags.md)
  Options used to control binary convolution kernels.
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./init%28source,weights,outputbiasterms,outputscaleterms,inputbiasterms,inputscaleterms,type,flags%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryconvolutionnode/init(source:weights:scalevalue:type:flags:))*