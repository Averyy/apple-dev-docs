---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loraconfiguration/loraparameters-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LoRAConfiguration.LoRAParameters

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct LoRAParameters
```

## Topics

### Initializers
- [init(from: Decoder) throws](./loraparameters-swift.struct/init%28from%29.md)
- [init(rank: Int, scale: Float, dropout: Float, keys: [String]?)](./loraparameters-swift.struct/init%28rank,scale,dropout,keys%29.md)
### Instance Properties
- [let dropout: Float](./loraparameters-swift.struct/dropout.md)
  Probability of dropping LoRA inputs during training. Disabled in evaluation mode.
- [let keys: [String]?](./loraparameters-swift.struct/keys.md)
- [let rank: Int](./loraparameters-swift.struct/rank.md)
- [let scale: Float](./loraparameters-swift.struct/scale.md)
### Default Implementations
- [Encodable Implementations](./loraparameters-swift.struct/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loraconfiguration/loraparameters-swift.struct)*