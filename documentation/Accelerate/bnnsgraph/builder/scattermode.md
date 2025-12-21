# BNNSGraph.Builder.ScatterMode

**Framework**: Accelerate  
**Kind**: enum

Constants that specify how scatter operations overwrite destination elements.

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
enum ScatterMode
```

## Topics

### Enumeration Cases
- [BNNSGraph.Builder.ScatterMode.add](bnnsgraph/builder/scattermode/add.md)
  The operation adds existing values to scattered values.
- [BNNSGraph.Builder.ScatterMode.divide](bnnsgraph/builder/scattermode/divide.md)
  The operation divides scattered values by existing values.
- [BNNSGraph.Builder.ScatterMode.maximum](bnnsgraph/builder/scattermode/maximum.md)
  The operation writes the maximum of the existing value and the scattered value.
- [BNNSGraph.Builder.ScatterMode.minimum](bnnsgraph/builder/scattermode/minimum.md)
  The operation writes the minimum of the existing value and the scattered value.
- [BNNSGraph.Builder.ScatterMode.multiply](bnnsgraph/builder/scattermode/multiply.md)
  The operation multiplies existing values by scattered values.
- [BNNSGraph.Builder.ScatterMode.subtract](bnnsgraph/builder/scattermode/subtract.md)
  The operation subtracts scattered values from existing values.
- [BNNSGraph.Builder.ScatterMode.update](bnnsgraph/builder/scattermode/update.md)
  The operation overwrites existing values with scattered values.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/scattermode)*