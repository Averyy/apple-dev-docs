# BNNSGraph.Builder.ConvolutionPadding

**Framework**: Accelerate  
**Kind**: enum

The padding that you use for convolution operations to specify zero-padding.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
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
- [BNNSGraph.Builder.ConvolutionPadding.custom(padding:)](bnnsgraph/builder/convolutionpadding/custom(padding:).md)
  Custom padding
- [BNNSGraph.Builder.ConvolutionPadding.lower](bnnsgraph/builder/convolutionpadding/lower.md)
  Pad the output to look like the input but prefer padding on the top and left.
- [BNNSGraph.Builder.ConvolutionPadding.same](bnnsgraph/builder/convolutionpadding/same.md)
  Pad the output to look like the input
- [BNNSGraph.Builder.ConvolutionPadding.valid](bnnsgraph/builder/convolutionpadding/valid.md)
  No padding

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/convolutionpadding)*