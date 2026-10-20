# MPSCNNSoftMaxGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A gradient softmax filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNSoftMaxGradient
```

```objc
@interface MPSCNNSoftMaxGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnsoftmaxgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpscnnsoftmaxgradient/init%28device%29.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](./mpscnngradientkernel.md)
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

### Softmax Layers
- [class MPSCNNSoftMax](./mpscnnsoftmax.md)
  A neural transfer function that is useful for classification tasks.
- [class MPSCNNLogSoftMax](./mpscnnlogsoftmax.md)
  A neural transfer function that  is useful for constructing a loss function to be minimized when training neural networks.
- [class MPSCNNLogSoftMaxGradient](./mpscnnlogsoftmaxgradient.md)
  A gradient logarithmic softmax filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsoftmaxgradient)*