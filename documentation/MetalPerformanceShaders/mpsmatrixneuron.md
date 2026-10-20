# MPSMatrixNeuron

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A neuron activation kernel that operates on matrices.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixNeuron
```

```objc
@interface MPSMatrixNeuron : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixneuron/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixneuron/init%28device%29.md)
### Instance Properties
- [var alpha: Double](./mpsmatrixneuron/alpha.md)
- [var sourceInputFeatureChannels: Int](./mpsmatrixneuron/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](./mpsmatrixneuron/sourcenumberoffeaturevectors.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixneuron/copy%28with,device%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultMatrix: MPSMatrix)](./mpsmatrixneuron/encode%28commandbuffer,inputmatrix,biasvector,resultmatrix%29.md)
- [func neuronParameterA() -> Float](./mpsmatrixneuron/neuronparametera%28%29.md)
- [func neuronParameterB() -> Float](./mpsmatrixneuron/neuronparameterb%28%29.md)
- [func neuronParameterC() -> Float](./mpsmatrixneuron/neuronparameterc%28%29.md)
- [func neuronType() -> MPSCNNNeuronType](./mpsmatrixneuron/neurontype%28%29.md)
- [func setNeuronToPReLUWithParametersA(Data)](./mpsmatrixneuron/setneurontopreluwithparametersa%28_%29.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](./mpsmatrixneuron/setneurontype%28_,parametera,parameterb,parameterc%29.md)

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

### Matrix Neural Network Operations
- [class MPSMatrixFullyConnected](./mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixFullyConnectedGradient](./mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuronGradient](./mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneuron)*