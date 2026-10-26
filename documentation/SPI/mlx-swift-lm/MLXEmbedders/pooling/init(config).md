---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling/init(config:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# init(config:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: init  
**Role**: Initializer

Initializes a `Pooling` module from a `PoolingConfiguration`.

## Declaration

```swift
init(config: PoolingConfiguration)
```

#### Discussion

The initialization follows a priority order: CLS > Mean > Max > Last. If no specific mode is enabled in the config, it defaults to `.first`.

## Parameters

- `config`: The configuration object containing pooling flags.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling/init(config:))*