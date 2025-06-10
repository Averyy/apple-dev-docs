# cast(to:)

**Framework**: Accelerate  
**Kind**: method

Adds a cast operation to the current graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func cast<U>(to type: U.Type) -> BNNSGraph.Builder.Tensor<U> where U : BNNSScalar
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/cast(to:))*