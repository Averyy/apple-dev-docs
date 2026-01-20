# MPSMatrixFullyConnectedGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixfullyconnectedgradient/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixfullyconnectedgradient/init(device:).md)
### Instance Properties
- [var alpha: Double](mpsmatrixfullyconnectedgradient/alpha.md)
- [var sourceInputFeatureChannels: Int](mpsmatrixfullyconnectedgradient/sourceinputfeaturechannels.md)
- [var sourceNumberOfFeatureVectors: Int](mpsmatrixfullyconnectedgradient/sourcenumberoffeaturevectors.md)
- [var sourceOutputFeatureChannels: Int](mpsmatrixfullyconnectedgradient/sourceoutputfeaturechannels.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixfullyconnectedgradient/copy(with:device:).md)
- [func encodeForData(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, weightMatrix: MPSMatrix, resultGradientForDataMatrix: MPSMatrix)](mpsmatrixfullyconnectedgradient/encodefordata(to:gradientmatrix:weightmatrix:resultgradientfordatamatrix:).md)
- [func encodeForWeightsAndBias(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, resultGradientForWeightMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)](mpsmatrixfullyconnectedgradient/encodeforweightsandbias(to:gradientmatrix:inputmatrix:resultgradientforweightmatrix:resultgradientforbiasvector:).md)

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
- [class MPSMatrixNeuron](mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.
- [class MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnectedgradient)*