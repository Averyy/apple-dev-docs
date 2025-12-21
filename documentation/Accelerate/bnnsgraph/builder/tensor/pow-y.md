# pow(y:)

**Framework**: Accelerate  
**Kind**: method

Adds an element-wise power operation to the current graph.

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
func pow(y: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function performs the operation `pow(self, y)`.

- Parameter `y`: The  the exponent values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/pow(y:))*