# setBatchNormalizationParametersForInferenceWithMean(_:variance:gamma:beta:epsilon:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setBatchNormalizationParametersForInferenceWithMean(_ mean: UnsafePointer<Float>?, variance: UnsafePointer<Float>?, gamma: UnsafePointer<Float>?, beta: UnsafePointer<Float>?, epsilon: Float)
```

```objc
- (void) setBatchNormalizationParametersForInferenceWithMean:(const float *) mean variance:(const float *) variance gamma:(const float *) gamma beta:(const float *) beta epsilon:(const float) epsilon;
```

## See Also

### Instance Methods
- [func encode(with: NSCoder)](./encode%28with%29.md)
- [func setNeuronToPReLUWithParametersA(Data)](./setneurontopreluwithparametersa%28_%29.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float)](./setneurontype%28_,parametera,parameterb%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/setbatchnormalizationparametersforinferencewithmean(_:variance:gamma:beta:epsilon:))*