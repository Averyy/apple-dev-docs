# MPSCNNNeuronAbsolute

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

An absolute neuron filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNNeuronAbsolute
```

```objc
@interface MPSCNNNeuronAbsolute : MPSCNNNeuron
```

## Overview

For each pixel in an image, the filter applies the following function:

![f(x) = | x |](https://developer.apple.com/tutorials/images/com.apple.metalperformanceshaders/media-2903538@2x.png)

## Topics

### Initializers
- [init(device: any MTLDevice)](./mpscnnneuronabsolute/init%28device%29.md)
  Initializes an absolute neuron filter.

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
- [class MPSCNNNeuronReLU](./mpscnnneuronrelu.md)
  A ReLU (Rectified Linear Unit) neuron filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronabsolute)*