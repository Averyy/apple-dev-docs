---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/audiofeatures(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# audioFeatures(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func audioFeatures(_ features: MLXArray) throws -> MLXArray?
```

#### Return Value

`[1, soft tokens, hidden]` features that fill its placeholder tokens, or `nil` when this checkpoint has no audio encoder.

#### Discussion

> **Throws**: Loading errors, or `OnDemandComponentError` if audio was excluded.

## Parameters

- `features`: `[frames, featureSize]` log-mel features of one audio.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/audiofeatures(_:))*