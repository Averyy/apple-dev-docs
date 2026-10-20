# MPSGraphRNNActivation

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

The activation modes for RNN operations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphRNNActivation
```

```c
enum MPSGraphRNNActivation : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSGraphRNNActivation.hardSigmoid](./mpsgraphrnnactivation/hardsigmoid.md)
  Defines a Hard sigmoid activation.
- [MPSGraphRNNActivation.none](./mpsgraphrnnactivation/none.md)
  Defines a pass through activation.
- [MPSGraphRNNActivation.relu](./mpsgraphrnnactivation/relu.md)
  Defines a ReLU activation.
- [MPSGraphRNNActivation.sigmoid](./mpsgraphrnnactivation/sigmoid.md)
  Defines a Sigmoid activation.
- [MPSGraphRNNActivation.tanh](./mpsgraphrnnactivation/tanh.md)
  Defines a Tanh activation.
### Initializers
- [init?(rawValue: UInt)](./mpsgraphrnnactivation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrnnactivation)*