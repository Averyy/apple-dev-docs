# MPSMatrixFullyConnectedGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel for applying a fully gradient connected neural network layer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixFullyConnectedGradient
```

```objc
@interface MPSMatrixFullyConnectedGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixfullyconnectedgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixfullyconnectedgradient/init%28device%29.md)
### Instance Properties
- [var alpha: Double](./mpsmatrixfullyconnectedgradient/alpha.md)
- [var sourceInputFeatureChannels: Int](./mpsmatrixfullyconnectedgradient/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](./mpsmatrixfullyconnectedgradient/sourcenumberoffeaturevectors.md)
- [var sourceOutputFeatureChannels: Int](./mpsmatrixfullyconnectedgradient/sourceoutputfeaturechannels.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixfullyconnectedgradient/copy%28with,device%29.md)
- [func encodeForData(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, weightMatrix: MPSMatrix, resultGradientForDataMatrix: MPSMatrix)](./mpsmatrixfullyconnectedgradient/encodefordata%28to,gradientmatrix,weightmatrix,resultgradientfordatamatrix%29.md)
- [func encodeForWeightsAndBias(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, resultGradientForWeightMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)](./mpsmatrixfullyconnectedgradient/encodeforweightsandbias%28to,gradientmatrix,inputmatrix,resultgradientforweightmatrix,resultgradientforbiasvector%29.md)

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
- [class MPSMatrixNeuron](./mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.
- [class MPSMatrixNeuronGradient](./mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnectedgradient)*