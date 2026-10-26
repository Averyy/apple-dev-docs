---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertconfiguration"
framework: "mlx-swift-lm/MLXEmbedders"
---

# BertConfiguration

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: struct  
**Role**: Structure

Configuration parameters for BERT and DistilBERT models.

## Declaration

```swift
struct BertConfiguration
```

#### Overview

This struct supports `Decodable` to allow direct initialization from a JSON configuration file. It handles the discrepancy between BERT and DistilBERT JSON keys (e.g., BERT’s `hidden_size` vs DistilBERT’s `dim`).

## Topics

### Initializers
- [init(from: Decoder) throws](./bertconfiguration/init%28from%29.md)
  Custom initializer to bridge different JSON schemas into a unified struct.

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertconfiguration)*