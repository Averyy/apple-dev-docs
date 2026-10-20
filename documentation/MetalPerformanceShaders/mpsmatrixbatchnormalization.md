# MPSMatrixBatchNormalization

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A batch normalization kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixBatchNormalization
```

```objc
@interface MPSMatrixBatchNormalization : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixbatchnormalization/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixbatchnormalization/init%28device%29.md)
### Instance Properties
- [var computeStatistics: Bool](./mpsmatrixbatchnormalization/computestatistics.md)
- [var epsilon: Float](./mpsmatrixbatchnormalization/epsilon.md)
- [var sourceInputFeatureChannels: Int](./mpsmatrixbatchnormalization/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](./mpsmatrixbatchnormalization/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixbatchnormalization/copy%28with,device%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, meanVector: MPSVector, varianceVector: MPSVector, gammaVector: MPSVector?, betaVector: MPSVector?, resultMatrix: MPSMatrix)](./mpsmatrixbatchnormalization/encode%28commandbuffer,inputmatrix,meanvector,variancevector,gammavector,betavector,resultmatrix%29.md)
- [func neuronParameterA() -> Float](./mpsmatrixbatchnormalization/neuronparametera%28%29.md)
- [func neuronParameterB() -> Float](./mpsmatrixbatchnormalization/neuronparameterb%28%29.md)
- [func neuronParameterC() -> Float](./mpsmatrixbatchnormalization/neuronparameterc%28%29.md)
- [func neuronType() -> MPSCNNNeuronType](./mpsmatrixbatchnormalization/neurontype%28%29.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](./mpsmatrixbatchnormalization/setneurontype%28_,parametera,parameterb,parameterc%29.md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](./mpsmatrixunarykernel.md)
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
- [class MPSMatrixBatchNormalizationGradient](./mpsmatrixbatchnormalizationgradient.md)
  A batch normalization gradient kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbatchnormalization)*