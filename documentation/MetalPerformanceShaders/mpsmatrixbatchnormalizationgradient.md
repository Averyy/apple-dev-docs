# MPSMatrixBatchNormalizationGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSMatrixBatchNormalizationGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixbatchnormalizationgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixbatchnormalizationgradient/init%28device%29.md)
### Instance Properties
- [var epsilon: Float](./mpsmatrixbatchnormalizationgradient/epsilon.md)
- [var sourceInputFeatureChannels: Int](./mpsmatrixbatchnormalizationgradient/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](./mpsmatrixbatchnormalizationgradient/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixbatchnormalizationgradient/copy%28with,device%29.md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, mean: MPSVector, varianceVector: MPSVector, gammaVector: MPSVector?, betaVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForGammaVector: MPSVector?, resultGradientForBetaVector: MPSVector?)](./mpsmatrixbatchnormalizationgradient/encode%28to,gradientmatrix,inputmatrix,mean,variancevector,gammavector,betavector,resultgradientfordatamatrix,resultgradientforgammavector,resultgradientforbetavector%29.md)
- [func neuronParameterA() -> Float](./mpsmatrixbatchnormalizationgradient/neuronparametera%28%29.md)
- [func neuronParameterB() -> Float](./mpsmatrixbatchnormalizationgradient/neuronparameterb%28%29.md)
- [func neuronParameterC() -> Float](./mpsmatrixbatchnormalizationgradient/neuronparameterc%28%29.md)
- [func neuronType() -> MPSCNNNeuronType](./mpsmatrixbatchnormalizationgradient/neurontype%28%29.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](./mpsmatrixbatchnormalizationgradient/setneurontype%28_,parametera,parameterb,parameterc%29.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](./mpsmatrixbinarykernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Matrix Normalization Operations
- [class MPSMatrixBatchNormalization](./mpsmatrixbatchnormalization.md)
  A batch normalization kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbatchnormalizationgradient)*