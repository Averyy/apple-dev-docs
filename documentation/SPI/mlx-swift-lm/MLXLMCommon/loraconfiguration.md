---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loraconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LoRAConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Configuration for how LoRA or DoRA should be applied.

## Declaration

```swift
struct LoRAConfiguration
```

## Overview

Note: It’s compatible with `adapter_config.json` file created during training using MLX libraries.

Example:

```json
{
  "fine_tune_type": "lora",
  "num_layers": 28,
  "lora_parameters": {
    "rank": 16,
    "dropout": 0.05,
    "scale": 20.0
  }
}
```

## Topics

### Structures
- [LoRAConfiguration.LoRAParameters](./loraconfiguration/loraparameters-swift.struct.md)
### Initializers
- [init(from: any Decoder) throws](./loraconfiguration/init%28from%29.md)
- [init(numLayers: Int, fineTuneType: FineTuneType, loraParameters: LoRAParameters)](./loraconfiguration/init%28numlayers,finetunetype,loraparameters%29.md)
### Instance Properties
- [let fineTuneType: FineTuneType](./loraconfiguration/finetunetype-swift.property.md)
- [let loraParameters: LoRAParameters](./loraconfiguration/loraparameters-swift.property.md)
- [let numLayers: Int](./loraconfiguration/numlayers.md)
### Enumerations
- [LoRAConfiguration.FineTuneType](./loraconfiguration/finetunetype-swift.enum.md)
### Default Implementations
- [Encodable Implementations](./loraconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loraconfiguration)*