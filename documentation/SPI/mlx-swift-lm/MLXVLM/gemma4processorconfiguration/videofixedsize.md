---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processorconfiguration/videofixedsize"
framework: "mlx-swift-lm/MLXVLM"
---

# videoFixedSize

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: property  
**Role**: Instance Property

Video frames use a smaller square (a multiple of patch_size * pooling_kernel_size = 48) so the vision tower’s leading pooled tokens cover the frame within the ~70-token video budget: 432 → 27x27 patches → 81 pooled tokens, trimmed to `visionSoftTokensPerVideoFrame` (70) in the model.

## Declaration

```swift
var videoFixedSize: CGSize { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processorconfiguration/videofixedsize)*