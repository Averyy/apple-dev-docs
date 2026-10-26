---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/pairwiserotation/rotate(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# rotate(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Apply channel scaling + pairwise Givens rotations to the last axis.

## Declaration

```swift
func rotate(_ x: MLXArray) -> MLXArray
```

#### Discussion

Accepts any leading shape (the MoE path passes gathered 4-D activations); the input is flattened to 2-D for the kernel and the original shape is restored on return. Empty batches pass through unchanged (guarded in `dispatchPairwiseRotation`). No mutable state is read or written by this method.

Kernel selection lives in `dispatchPairwiseRotation`: groupSize == 128 takes the simdgroup-resident kernel, any other group size the generic fallback specialised on that size.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/pairwiserotation/rotate(_:))*