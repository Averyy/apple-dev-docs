# MPSMatrixFullyConnected

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel for applying a fully connected neural network layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixFullyConnected
```

```objc
@interface MPSMatrixFullyConnected : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixfullyconnected/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixfullyconnected/init%28device%29.md)
### Instance Properties
- [var alpha: Double](./mpsmatrixfullyconnected/alpha.md)
- [var sourceInputFeatureChannels: Int](./mpsmatrixfullyconnected/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](./mpsmatrixfullyconnected/sourcenumberoffeaturevectors.md)
- [var sourceOutputFeatureChannels: Int](./mpsmatrixfullyconnected/sourceoutputfeaturechannels.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixfullyconnected/copy%28with,device%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, weightMatrix: MPSMatrix, biasVector: MPSVector?, resultMatrix: MPSMatrix)](./mpsmatrixfullyconnected/encode%28commandbuffer,inputmatrix,weightmatrix,biasvector,resultmatrix%29.md)
- [func neuronParameterA() -> Float](./mpsmatrixfullyconnected/neuronparametera%28%29.md)
- [func neuronParameterB() -> Float](./mpsmatrixfullyconnected/neuronparameterb%28%29.md)
- [func neuronParameterC() -> Float](./mpsmatrixfullyconnected/neuronparameterc%28%29.md)
- [func neuronType() -> MPSCNNNeuronType](./mpsmatrixfullyconnected/neurontype%28%29.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](./mpsmatrixfullyconnected/setneurontype%28_,parametera,parameterb,parameterc%29.md)

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
- [class MPSMatrixFullyConnectedGradient](./mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuron](./mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.
- [class MPSMatrixNeuronGradient](./mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnected)*