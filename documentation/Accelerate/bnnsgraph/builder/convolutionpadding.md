# BNNSGraph.Builder.ConvolutionPadding

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

The padding that you use for convolution operations to specify zero-padding.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum ConvolutionPadding
```

## Topics

### Enumeration Cases
- [BNNSGraph.Builder.ConvolutionPadding.custom(padding:)](./convolutionpadding/custom%28padding%29.md)
  Custom padding
- [BNNSGraph.Builder.ConvolutionPadding.lower](./convolutionpadding/lower.md)
  Pad the output to look like the input but prefer padding on the top and left.
- [BNNSGraph.Builder.ConvolutionPadding.same](./convolutionpadding/same.md)
  Pad the output to look like the input
- [BNNSGraph.Builder.ConvolutionPadding.valid](./convolutionpadding/valid.md)
  No padding

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/convolutionpadding)*