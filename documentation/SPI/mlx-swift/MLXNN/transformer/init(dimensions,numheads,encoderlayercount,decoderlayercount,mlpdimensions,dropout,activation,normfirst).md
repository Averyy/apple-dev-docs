---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/transformer/init(dimensions:numheads:encoderlayercount:decoderlayercount:mlpdimensions:dropout:activation:normfirst:)"
framework: "mlx-swift/MLXNN"
---

# init(dimensions:numHeads:encoderLayerCount:decoderLayerCount:mlpDimensions:dropout:activation:normFirst:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Initialize the transformer.

## Declaration

```swift
init(dimensions: Int = 512, numHeads: Int = 8, encoderLayerCount: Int = 6, decoderLayerCount: Int = 6, mlpDimensions: Int? = nil, dropout: Float = 0.0, activation: any UnaryLayer = ReLU(), normFirst: Bool = false)
```

## Parameters

- `dimensions`: Number of expected features in the encoder/decoder
- `numHeads`: Number of attention heads
- `encoderLayerCount`: Number of layers in the encoder
- `decoderLayerCount`: Number of layers in the decoder
- `mlpDimensions`: Hidden dimensions of the MLP block in each layer.  Defaults to `4 * dimensions` if not specified
- `dropout`: Dropout value for the encode and decoder.  Dropout is used after each attention layer and the activation in the MLP layer
- `activation`: The activation layer for the MLP hidden layer
- `normFirst`: If `true` encode and decoder layers will perform layer normalization before attention and MLP operations, otherwise after


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/transformer/init(dimensions:numheads:encoderlayercount:decoderlayercount:mlpdimensions:dropout:activation:normfirst:))*