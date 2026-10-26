---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessor/preprocess(image:processing:)"
framework: "mlx-swift-lm/MLXVLM"
---

# preprocess(image:processing:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Resizes, normalizes and patchifies one image.

## Declaration

```swift
func preprocess(image: CIImage, processing: UserInput.Processing?) throws -> (MLXArray, THW)
```

#### Discussion

The patch layout is `(temporal, channels, patchH, patchW)` inside each token and the tokens themselves are in plain raster order — both differ from `QwenVL.patchify`, and both matter because the vision tower does its own 2×2 merge grouping downstream.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessor/preprocess(image:processing:))*