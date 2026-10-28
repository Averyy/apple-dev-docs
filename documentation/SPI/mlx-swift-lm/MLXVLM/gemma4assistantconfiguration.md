---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantconfiguration"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4AssistantConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

Configuration for the Gemma 4 MTP speculative drafter.

## Declaration

```swift
struct Gemma4AssistantConfiguration
```

## Overview

Mirrors mlx-vlm’s `Gemma4AssistantConfig` (`mlx_vlm/speculative/drafters/gemma4_assistant/config.py` at SHA d49d428). Decodes from a HF `config.json` shape.

## Topics

### Initializers
- [init(from: any Swift.Decoder) throws](./gemma4assistantconfiguration/init%28from%29.md)
### Instance Properties
- [let backboneHiddenSize: Int](./gemma4assistantconfiguration/backbonehiddensize.md)
- [let blockSize: Int](./gemma4assistantconfiguration/blocksize.md)
- [let centroidIntermediateTopK: Int](./gemma4assistantconfiguration/centroidintermediatetopk.md)
- [let modelType: String](./gemma4assistantconfiguration/modeltype.md)
- [let numCentroids: Int](./gemma4assistantconfiguration/numcentroids.md)
- [let targetLayerIds: [Int]](./gemma4assistantconfiguration/targetlayerids.md)
  Per mlx-vlm config.py: unused by MTP (drafter consumes shared K/V, not per-layer hidden captures) but kept for API parity with DFlash.
- [let textConfiguration: Gemma4TextConfiguration](./gemma4assistantconfiguration/textconfiguration.md)
- [let tieWordEmbeddings: Bool](./gemma4assistantconfiguration/tiewordembeddings.md)
- [let useOrderedEmbeddings: Bool](./gemma4assistantconfiguration/useorderedembeddings.md)
### Default Implementations
- [Encodable Implementations](./gemma4assistantconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantconfiguration)*