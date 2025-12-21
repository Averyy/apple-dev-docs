# pad(_:padding:)

**Framework**: Accelerate  
**Kind**: method

Adds a padding operation to the graph

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
func pad(_ type: BNNSGraph.Builder.Padding, padding: [Int]) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `type`: The padding type.
- `padding`: An array of integer values that contains an even count of elements. Each   contiguous pair of elements specifies the before (for example, top or left) and after (for example, bottom   or right) padding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/pad(_:padding:))*