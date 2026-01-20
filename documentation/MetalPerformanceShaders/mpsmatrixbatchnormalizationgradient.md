# MPSMatrixBatchNormalizationGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A batch normalization gradient kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixBatchNormalizationGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixbatchnormalizationgradient/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixbatchnormalizationgradient/init(device:).md)
### Instance Properties
- [var epsilon: Float](mpsmatrixbatchnormalizationgradient/epsilon.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixbatchnormalizationgradient/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixbatchnormalizationgradient/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixbatchnormalizationgradient/copy(with:device:).md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, mean: MPSVector, varianceVector: MPSVector, gammaVector: MPSVector?, betaVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForGammaVector: MPSVector?, resultGradientForBetaVector: MPSVector?)](mpsmatrixbatchnormalizationgradient/encode(to:gradientmatrix:inputmatrix:mean:variancevector:gammavector:betavector:resultgradientfordatamatrix:resultgradientforgammavector:resultgradientforbetavector:).md)
- [func neuronParameterA() -> Float](mpsmatrixbatchnormalizationgradient/neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixbatchnormalizationgradient/neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixbatchnormalizationgradient/neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixbatchnormalizationgradient/neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixbatchnormalizationgradient/setneurontype(_:parametera:parameterb:parameterc:).md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSMatrixBatchNormalization](mpsmatrixbatchnormalization.md)
  A batch normalization kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbatchnormalizationgradient)*