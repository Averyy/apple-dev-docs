---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/processing-swift.struct/minpixels"
framework: "mlx-swift-lm/MLXLMCommon"
---

# minPixels

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Optional per-call overrides for the image resize budget. When set, they replace the model’s configured `min_pixels` / `max_pixels` for this request; when `nil` the model configuration is used. This lets a caller request the resolution a model was tuned for without hard-coding pixel counts in the processor.

## Declaration

```swift
var minPixels: Int?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/processing-swift.struct/minpixels)*