# prelu(alpha:)

**Framework**: Accelerate  
**Kind**: method

Adds a Parametric ReLU (PReLU) activation operation to the current graph.

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
func prelu(alpha: [Float]) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

Performs the operation `prelu(self) = max(0, self) + alpha[i] * min(0, self)`, for each channel `i`.

`self` must have at least two dimensions.

The number of elements in `alpha` must be either 1 or `self.shape[1]`.

The operation applies the weight `alpha[i]` to channel `i` while performing the activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/prelu(alpha:))*