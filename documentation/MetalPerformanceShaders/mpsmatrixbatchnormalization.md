# MPSMatrixBatchNormalization

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixbatchnormalization/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixbatchnormalization/init(device:).md)
### Instance Properties
- [var computeStatistics: Bool](mpsmatrixbatchnormalization/computestatistics.md)
- [var epsilon: Float](mpsmatrixbatchnormalization/epsilon.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixbatchnormalization/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixbatchnormalization/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixbatchnormalization/copy(with:device:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, meanVector: MPSVector, varianceVector: MPSVector, gammaVector: MPSVector?, betaVector: MPSVector?, resultMatrix: MPSMatrix)](mpsmatrixbatchnormalization/encode(commandbuffer:inputmatrix:meanvector:variancevector:gammavector:betavector:resultmatrix:).md)
- [func neuronParameterA() -> Float](mpsmatrixbatchnormalization/neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixbatchnormalization/neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixbatchnormalization/neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixbatchnormalization/neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixbatchnormalization/setneurontype(_:parametera:parameterb:parameterc:).md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
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

- [class MPSMatrixBatchNormalizationGradient](mpsmatrixbatchnormalizationgradient.md)
  A batch normalization gradient kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbatchnormalization)*