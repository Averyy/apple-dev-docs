# MPSCNNNeuronReLU

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A ReLU (Rectified Linear Unit) neuron filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNNeuronReLU
```

```objc
@interface MPSCNNNeuronReLU : MPSCNNNeuron
```

#### Overview

For each pixel in an image, the filter applies the following function:

![f(x) = x if x >= 0 | a * x if x < 0](https://developer.apple.com/tutorials/images/com.apple.metalperformanceshaders/media-2903544@2x.png)

This filter is called *l__eaky ReLU* in CNN literature. Some CNN literature defines *classical* *ReLU* as `max(0, x)`. If you want this behavior, simply set the `a` property to `0`.

## Topics

### Initializers
- [init(device: any MTLDevice, a: Float)](./mpscnnneuronrelu/init%28device,a%29.md)
  Initializes a ReLU neuron filter.

## Relationships

### Inherits From
- [MPSCNNNeuron](./mpscnnneuron.md)
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

### Neuron Layers
- [class MPSCNNNeuronAbsolute](./mpscnnneuronabsolute.md)
  An absolute neuron filter.
- [class MPSCNNNeuronELU](./mpscnnneuronelu.md)
  A parametric ELU neuron filter.
- [class MPSCNNNeuronHardSigmoid](./mpscnnneuronhardsigmoid.md)
  A hard sigmoid neuron filter.
- [class MPSCNNNeuronLinear](./mpscnnneuronlinear.md)
  A linear neuron filter.
- [class MPSCNNNeuronPReLU](./mpscnnneuronprelu.md)
  A parametric ReLU (Rectified Linear Unit) neuron filter.
- [class MPSCNNNeuronReLUN](./mpscnnneuronrelun.md)
  A ReLUN neuron filter.
- [class MPSCNNNeuronSigmoid](./mpscnnneuronsigmoid.md)
  A sigmoid neuron filter.
- [class MPSCNNNeuronSoftPlus](./mpscnnneuronsoftplus.md)
  A parametric softplus neuron filter.
- [class MPSCNNNeuronSoftSign](./mpscnnneuronsoftsign.md)
  A softsign neuron filter.
- [class MPSCNNNeuronTanH](./mpscnnneurontanh.md)
  A hyperbolic tangent neuron filter.
- [class MPSCNNNeuron](./mpscnnneuron.md)
  A filter that applies a neuron activation function.
- [class MPSCNNNeuronExponential](./mpscnnneuronexponential.md)
  An exponential neuron filter.
- [class MPSCNNNeuronGradient](./mpscnnneurongradient.md)
  A gradient neuron filter.
- [class MPSCNNNeuronLogarithm](./mpscnnneuronlogarithm.md)
  A logarithm neuron filter.
- [class MPSCNNNeuronPower](./mpscnnneuronpower.md)
  A power neuron filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronrelu)*