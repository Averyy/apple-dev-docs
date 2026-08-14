# MPSCNNSoftMax

**Framework**: Metal Performance Shaders  
**Kind**: class

A neural transfer function that is useful for classification tasks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSoftMax
```

#### Overview

The softmax filter is applied across feature channels in a convolutional manner at all spatial locations. The softmax filter can be seen as the combination of an activation function (exponential) and a normalization operator.

For each feature channel per pixel in an image in a feature map, the softmax filter computes the following:

![pixel = exp(pixel(x,y,k))/sum(exp(pixel(x,y,0)) … exp(pixel(x,y,N-1))](/images/com.apple.metalperformanceshaders/media-2903559@2x.png)

Where `R` is the result channel in the pixel and `N` is the number of feature channels.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSCNNLogSoftMax](mpscnnlogsoftmax.md)
  A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.
- [class MPSCNNLogSoftMaxGradient](mpscnnlogsoftmaxgradient.md)
  A gradient logarithmic softmax filter.
- [class MPSCNNSoftMaxGradient](mpscnnsoftmaxgradient.md)
  A gradient softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsoftmax)*