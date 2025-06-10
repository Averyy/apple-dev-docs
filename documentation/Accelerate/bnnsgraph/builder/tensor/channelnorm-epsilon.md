# channelNorm(epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds a channel normalization operation to the current graph.

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
func channelNorm(epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function performs channel normalization of `self`.`self` must be at least three-dimensional.

## Parameters

- `epsilon`: The epsilon value that the function uses to avoid division by zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/channelnorm(epsilon:))*