# cast(to:)

**Framework**: Accelerate  
**Kind**: method

Adds a cast operation to the current graph.

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
func cast<U>(to type: U.Type) -> BNNSGraph.Builder.Tensor<U> where U : BNNSScalar
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/cast(to:))*