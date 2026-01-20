# MPSNNNeuronDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

An object that specifies properties used by a neuron kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNNeuronDescriptor
```

## Topics

### Instance Properties
- [var a: Float](mpsnnneurondescriptor/a.md)
- [var b: Float](mpsnnneurondescriptor/b.md)
- [var c: Float](mpsnnneurondescriptor/c.md)
- [var data: Data?](mpsnnneurondescriptor/data.md)
- [var neuronType: MPSCNNNeuronType](mpsnnneurondescriptor/neurontype.md)
### Type Methods
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/cnnneurondescriptor(with:).md)
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType, a: Float) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/cnnneurondescriptor(with:a:).md)
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType, a: Float, b: Float) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/cnnneurondescriptor(with:a:b:).md)
- [class func cnnNeuronDescriptor(with: MPSCNNNeuronType, a: Float, b: Float, c: Float) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/cnnneurondescriptor(with:a:b:c:).md)
- [class func cnnNeuronPReLUDescriptor(with: Data, noCopy: Bool) -> MPSNNNeuronDescriptor](mpsnnneurondescriptor/cnnneuronpreludescriptor(with:nocopy:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class MPSCNNNeuronAbsolute](mpscnnneuronabsolute.md)
  An absolute neuron filter.
- [class MPSCNNNeuronELU](mpscnnneuronelu.md)
  A parametric ELU neuron filter.
- [class MPSCNNNeuronHardSigmoid](mpscnnneuronhardsigmoid.md)
  A hard sigmoid neuron filter.
- [class MPSCNNNeuronLinear](mpscnnneuronlinear.md)
  A linear neuron filter.
- [class MPSCNNNeuronPReLU](mpscnnneuronprelu.md)
  A parametric ReLU (Rectified Linear Unit) neuron filter.
- [class MPSCNNNeuronReLUN](mpscnnneuronrelun.md)
  A ReLUN neuron filter.
- [class MPSCNNNeuronReLU](mpscnnneuronrelu.md)
  A ReLU (Rectified Linear Unit) neuron filter.
- [class MPSCNNNeuronSigmoid](mpscnnneuronsigmoid.md)
  A sigmoid neuron filter.
- [class MPSCNNNeuronSoftPlus](mpscnnneuronsoftplus.md)
  A parametric softplus neuron filter.
- [class MPSCNNNeuronSoftSign](mpscnnneuronsoftsign.md)
  A softsign neuron filter.
- [class MPSCNNNeuronTanH](mpscnnneurontanh.md)
  A hyperbolic tangent neuron filter.
- [class MPSCNNNeuron](mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [class MPSCNNNeuronExponential](mpscnnneuronexponential.md)
  An exponential neuron filter.
- [class MPSCNNNeuronGradient](mpscnnneurongradient.md)
  A gradient neuron filter.
- [class MPSCNNNeuronLogarithm](mpscnnneuronlogarithm.md)
  A logarithm neuron filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnneurondescriptor)*