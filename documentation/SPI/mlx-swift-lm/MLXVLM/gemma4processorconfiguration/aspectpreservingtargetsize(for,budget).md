---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processorconfiguration/aspectpreservingtargetsize(for:budget:)"
framework: "mlx-swift-lm/MLXVLM"
---

# aspectPreservingTargetSize(for:budget:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Port of the Python Gemma4ImageProcessor’s aspect-ratio preserving resize: the largest dimensions that (a) stay within the patch budget maxSoftTokens * poolingKernelSize², and (b) keep both sides divisible by poolingKernelSize * patchSize, so the pooling kernel is exact and the pooled grid covers the image fully at any aspect ratio.

## Declaration

```swift
func aspectPreservingTargetSize(for imageSize: CGSize, budget: Int? = nil) -> CGSize
```

#### Discussion

Note the config’s `size` entry is deliberately ignored, as in the Python reference — models ship a vestigial 224x224 there.

## Parameters

- `imageSize`: Original image dimensions.
- `budget`: Soft tokens to fit; defaults to `maxSoftTokens`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processorconfiguration/aspectpreservingtargetsize(for:budget:))*