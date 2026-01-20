# MPSCNNLogSoftMax

**Framework**: Metal Performance Shaders  
**Kind**: class

A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLogSoftMax
```

#### Overview

The logarithmic softmax filter is calculated by taking the natural logarithm of the result of a softmax filter.

For each feature channel per pixel in an image in a feature map, the logarithmic softmax filter computes the following:

![pixel = pixel(x,y,k)) - ln{sum(exp(pixel(x,y,0)) … exp(pixel(x,y,N-1))}](https://docs-assets.developer.apple.com/published/dcbad99ffb71ffef8fde766ddf9b3650/media-2903560%402x.png)

Where `R` is the result channel in the pixel, `N` is the number of feature channels, and `y=ln(x)` satisfies `e``ʸ``=x`.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
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

- [class MPSCNNSoftMax](mpscnnsoftmax.md)
  A neural transfer function that is useful for classification tasks.
- [class MPSCNNLogSoftMaxGradient](mpscnnlogsoftmaxgradient.md)
  A gradient logarithmic softmax filter.
- [class MPSCNNSoftMaxGradient](mpscnnsoftmaxgradient.md)
  A gradient softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlogsoftmax)*