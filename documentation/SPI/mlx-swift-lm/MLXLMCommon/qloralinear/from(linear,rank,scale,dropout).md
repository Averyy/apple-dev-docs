---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qloralinear/from(linear:rank:scale:dropout:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# from(linear:rank:scale:dropout:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Convert a `QuantizedLinear` layer into a new `Linear` layer that implements the `LoRA` adapter.

## Declaration

```swift
static func from(linear: QuantizedLinear, rank: Int = 8, scale: Float = 20.0, dropout: Float = 0.0) -> LoRALayer
```

#### Discussion

This is typically called via `LoRATrain.convert(model:layers:)`.

##### See Also

- [`from(linear:rank:scale:dropout:)`](../loralinear/from%28linear,rank,scale,dropout%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qloralinear/from(linear:rank:scale:dropout:))*