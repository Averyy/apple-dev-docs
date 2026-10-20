# MPSMatrixNeuronGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSMatrixNeuronGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixneurongradient/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixneurongradient/init%28device%29.md)
### Instance Properties
- [var alpha: Double](./mpsmatrixneurongradient/alpha.md)
- [var sourceInputFeatureChannels: Int](./mpsmatrixneurongradient/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](./mpsmatrixneurongradient/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixneurongradient/copy%28with,device%29.md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)](./mpsmatrixneurongradient/encode%28to,gradientmatrix,inputmatrix,biasvector,resultgradientfordatamatrix,resultgradientforbiasvector%29.md)
- [func neuronParameterA() -> Float](./mpsmatrixneurongradient/neuronparametera%28%29.md)
- [func neuronParameterB() -> Float](./mpsmatrixneurongradient/neuronparameterb%28%29.md)
- [func neuronParameterC() -> Float](./mpsmatrixneurongradient/neuronparameterc%28%29.md)
- [func neuronType() -> MPSCNNNeuronType](./mpsmatrixneurongradient/neurontype%28%29.md)
- [func setNeuronToPReLUWithParametersA(Data)](./mpsmatrixneurongradient/setneurontopreluwithparametersa%28_%29.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](./mpsmatrixneurongradient/setneurontype%28_,parametera,parameterb,parameterc%29.md)

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

### Matrix Neural Network Operations
- [class MPSMatrixFullyConnected](./mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixFullyConnectedGradient](./mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuron](./mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneurongradient)*