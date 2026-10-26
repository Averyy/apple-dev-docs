---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/poolingconfiguration"
framework: "mlx-swift-lm/MLXEmbedders"
---

# PoolingConfiguration

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: struct  
**Role**: Structure

Configuration for the `Pooling` layer, typically loaded from a JSON file.

## Declaration

```swift
struct PoolingConfiguration
```

#### Overview

This struct defines which pooling strategy to apply and the output dimensions, mapping keys from the standard `sentence-transformers` configuration format.

## Topics

### Initializers
- [init(from: any Decoder) throws](./poolingconfiguration/init%28from%29.md)
### Instance Properties
- [let dimension: Int](./poolingconfiguration/dimension.md)
  The target output dimension for the embeddings.
- [let poolingModeClsToken: Bool](./poolingconfiguration/poolingmodeclstoken.md)
  Whether to use the CLS token (special classification token) for pooling.
- [let poolingModeLastToken: Bool](./poolingconfiguration/poolingmodelasttoken.md)
  Whether to use the last token in the sequence for pooling.
- [let poolingModeMaxTokens: Bool](./poolingconfiguration/poolingmodemaxtokens.md)
  Whether to use the maximum value across sequence tokens for pooling.
- [let poolingModeMeanTokens: Bool](./poolingconfiguration/poolingmodemeantokens.md)
  Whether to use the mean of all sequence tokens for pooling.
### Default Implementations
- [Encodable Implementations](./poolingconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/poolingconfiguration)*