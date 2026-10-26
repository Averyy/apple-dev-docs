---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalconfiguration/mlxhead"
framework: "mlx-swift-lm/MLXEmbedders"
---

# LFM2BidirectionalConfiguration.MLXHead

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: struct  
**Role**: Structure

The custom `"mlx"` block that selects the retrieval head and carries the prompt/prefix conventions used by callers (the library does not inject them).

## Declaration

```swift
struct MLXHead
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./mlxhead/init%28from%29.md)
### Instance Properties
- [let documentLength: Int?](./mlxhead/documentlength.md)
- [let documentPrefix: String?](./mlxhead/documentprefix.md)
- [let head: Kind](./mlxhead/head.md)
- [let pooling: String?](./mlxhead/pooling.md)
- [let projDim: Int?](./mlxhead/projdim.md)
- [let prompts: [String : String]?](./mlxhead/prompts.md)
- [let queryLength: Int?](./mlxhead/querylength.md)
- [let queryPrefix: String?](./mlxhead/queryprefix.md)
### Enumerations
- [LFM2BidirectionalConfiguration.MLXHead.Kind](./mlxhead/kind.md)
### Default Implementations
- [Encodable Implementations](./mlxhead/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalconfiguration/mlxhead)*