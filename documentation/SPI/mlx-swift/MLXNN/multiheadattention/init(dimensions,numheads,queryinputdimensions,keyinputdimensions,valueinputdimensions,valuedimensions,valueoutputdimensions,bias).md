---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/multiheadattention/init(dimensions:numheads:queryinputdimensions:keyinputdimensions:valueinputdimensions:valuedimensions:valueoutputdimensions:bias:)"
framework: "mlx-swift/MLXNN"
---

# init(dimensions:numHeads:queryInputDimensions:keyInputDimensions:valueInputDimensions:valueDimensions:valueOutputDimensions:bias:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Implements the scaled dot product attention with multiple heads.

## Declaration

```swift
init(dimensions: Int, numHeads: Int, queryInputDimensions: Int? = nil, keyInputDimensions: Int? = nil, valueInputDimensions: Int? = nil, valueDimensions: Int? = nil, valueOutputDimensions: Int? = nil, bias: Bool = false)
```

## Discussion

Given inputs for queries, keys and values the [`MultiHeadAttention`](../multiheadattention.md) produces new values by aggregating information from the input values according to the similarities of the input queries and keys.

All inputs as well as the output are linearly projected without biases by default.

[`MultiHeadAttention`](../multiheadattention.md) also takes an optional additive attention mask that should be broadcastable with `(batch, numHeads, # queries, # keys)`. The mask should have `-inf` or very large negative numbers at the positions that should *not* be attended to.

### See Also

- ``createAdditiveCausalMask(_:dtype:)

## Parameters

- `dimensions`: Model dimensions and default for the other dimensions if they are not supplied
- `numHeads`: Number of attention heads
- `queryInputDimensions`: Input dimensions of queries
- `keyInputDimensions`: Input dimensions of keys
- `valueInputDimensions`: Input dimensions of values
- `valueDimensions`: Dimensions of values after the projection
- `valueOutputDimensions`: Dimensions new values will be projected to
- `bias`: If `true` uses a bias in the `Linear` layers


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/multiheadattention/init(dimensions:numheads:queryinputdimensions:keyinputdimensions:valueinputdimensions:valuedimensions:valueoutputdimensions:bias:))*