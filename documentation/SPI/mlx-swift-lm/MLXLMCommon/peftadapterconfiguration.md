---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/peftadapterconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PEFTAdapterConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

PEFT `adapter_config.json` schema. Only the fields we use are decoded.

## Declaration

```swift
struct PEFTAdapterConfiguration
```

## Topics

### Initializers
- [init(from: Decoder) throws](./peftadapterconfiguration/init%28from%29.md)
### Instance Properties
- [let loraAlpha: Float](./peftadapterconfiguration/loraalpha.md)
- [let loraDropout: Float](./peftadapterconfiguration/loradropout.md)
- [let peftType: String](./peftadapterconfiguration/pefttype.md)
- [let r: Int](./peftadapterconfiguration/r.md)
- [let targetModules: [String]](./peftadapterconfiguration/targetmodules.md)
- [let useDora: Bool](./peftadapterconfiguration/usedora.md)
### Default Implementations
- [Encodable Implementations](./peftadapterconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/peftadapterconfiguration)*