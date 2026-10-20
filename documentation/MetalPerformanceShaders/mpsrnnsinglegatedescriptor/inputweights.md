# inputWeights

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var inputWeights: (any MPSCNNConvolutionDataSource)? { get set }
```

```objc
@property (nonatomic, retain, readwrite, nullable) id<MPSCNNConvolutionDataSource> inputWeights;
```

## See Also

### Instance Properties
- [var recurrentWeights: (any MPSCNNConvolutionDataSource)?](./recurrentweights.md)
- [protocol MPSCNNConvolutionDataSource](../mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnsinglegatedescriptor/inputweights)*