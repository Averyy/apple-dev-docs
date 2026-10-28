---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcacheprotocol"
framework: "mlx-swift-lm/MLXLMCommon"
---

# QuantizedKVCacheProtocol

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for caches that support efficient quantized operations

## Declaration

```swift
protocol QuantizedKVCacheProtocol : KVCache
```

## Overview

**Usage Example:**

```swift
// Efficient quantized path
if let quantizedCache = cache as? QuantizedKVCacheProtocol {
    let (qKeys, qValues) = quantizedCache.updateQuantized(keys: k, values: v)
    // Use native quantized operations
    let scores = quantizedMM(queries, w: qKeys.0, scales: qKeys.1, biases: qKeys.2, ...)
} else {
    // Regular path
    let (k, v) = cache.update(keys: k, values: v)
    let output = MLXFast.scaledDotProductAttention(queries: q, keys: k, values: v, ...)
}
```

## Topics

### Instance Properties
- [var bits: Int](./quantizedkvcacheprotocol/bits.md)
  The number of quantization bits used
- [var groupSize: Int](./quantizedkvcacheprotocol/groupsize.md)
  The quantization group size used
- [var mode: QuantizationMode](./quantizedkvcacheprotocol/mode.md)
  Quantization mode
### Instance Methods
- [func getQuantizedState() -> ((MLXArray, MLXArray, MLXArray?), (MLXArray, MLXArray, MLXArray?))?](./quantizedkvcacheprotocol/getquantizedstate%28%29.md)
  Get current quantized state without updating
- [func updateQuantized(keys: MLXArray, values: MLXArray) -> ((MLXArray, MLXArray, MLXArray?), (MLXArray, MLXArray, MLXArray?))](./quantizedkvcacheprotocol/updatequantized%28keys,values%29.md)
  Update cache and return quantized tuples for maximum efficiency

## Relationships

### Inherits From
- [KVCache](./kvcache.md)
- MLX.Evaluatable
### Conforming Types
- [QuantizedKVCache](./quantizedkvcache.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcacheprotocol)*