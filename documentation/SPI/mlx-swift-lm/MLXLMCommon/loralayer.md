---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loralayer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LoRALayer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A protocol representing a module that includes a LoRA adapter and can be converted back to its original, unadapted form.

## Declaration

```swift
protocol LoRALayer : Module
```

## Topics

### Instance Properties
- [var loraEnabled: Bool](./loralayer/loraenabled.md)
  When false the layer behaves as the underlying base layer (no LoRA term added). Used by callers like `linearSpecGenerate` that need to toggle the adapter between draft and verify phases without unloading it.
### Instance Methods
- [func fused() -> Module](./loralayer/fused%28%29.md)
  Returns a version of the module with the LoRA adapter permanently fused in.
- [func reverted() -> Module](./loralayer/reverted%28%29.md)
  Returns the original module, without the LoRA adapter applied.

## Relationships

### Inherits From
- MLXNN.Module
### Conforming Types
- [DoRALinear](./doralinear.md)
- [LoRALinear](./loralinear.md)
- [QDoRALinear](./qdoralinear.md)
- [QLoRALinear](./qloralinear.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loralayer)*