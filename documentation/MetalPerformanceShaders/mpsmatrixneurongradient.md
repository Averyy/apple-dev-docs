# MPSMatrixNeuronGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient neuron activation kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixNeuronGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixneurongradient/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixneurongradient/init(device:).md)
### Instance Properties
- [var alpha: Double](mpsmatrixneurongradient/alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixneurongradient/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixneurongradient/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixneurongradient/copy(with:device:).md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)](mpsmatrixneurongradient/encode(to:gradientmatrix:inputmatrix:biasvector:resultgradientfordatamatrix:resultgradientforbiasvector:).md)
- [func neuronParameterA() -> Float](mpsmatrixneurongradient/neuronparametera.md)
- [func neuronParameterB() -> Float](mpsmatrixneurongradient/neuronparameterb.md)
- [func neuronParameterC() -> Float](mpsmatrixneurongradient/neuronparameterc.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixneurongradient/neurontype.md)
- [func setNeuronToPReLUWithParametersA(Data)](mpsmatrixneurongradient/setneurontopreluwithparametersa(_:).md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixneurongradient/setneurontype(_:parametera:parameterb:parameterc:).md)

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

- [class MPSMatrixFullyConnected](mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuron](mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneurongradient)*