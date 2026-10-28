---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/imagefeatures(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# imageFeatures(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func imageFeatures(_ pixels: MLXArray) throws -> MLXArray?
```

## Return Value

`[B, soft tokens, hidden]` features that fill their placeholder tokens, or `nil` when this checkpoint has no vision encoder.

## Discussion

> **Throws**: Loading errors, or `OnDemandComponentError` if vision was excluded.

## Parameters

- `pixels`: `[B, 3, H, W]` images or video frames of one size.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/imagefeatures(_:))*