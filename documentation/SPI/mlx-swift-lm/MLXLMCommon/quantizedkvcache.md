---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# QuantizedKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Quantized KV cache for memory efficiency using MLX quantization

## Declaration

```swift
class QuantizedKVCache
```

## Topics

### Initializers
- [init(groupSize: Int, bits: Int, mode: QuantizationMode)](./quantizedkvcache/init%28groupsize,bits,mode%29.md)
### Instance Properties
- [var bits: Int](./quantizedkvcache/bits.md)
- [var groupSize: Int](./quantizedkvcache/groupsize.md)
- [var isTrimmable: Bool](./quantizedkvcache/istrimmable.md)
- [var metaState: [String]](./quantizedkvcache/metastate.md)
- [let mode: QuantizationMode](./quantizedkvcache/mode.md)
- [var state: [MLXArray]](./quantizedkvcache/state.md)
  Array of keys and values – this will have either 6 elements or 4 elements (if biases are nil).
### Instance Methods
- [func copy() -> any KVCache](./quantizedkvcache/copy%28%29.md)
- [func getQuantizedState() -> ((MLXArray, MLXArray, MLXArray?), (MLXArray, MLXArray, MLXArray?))?](./quantizedkvcache/getquantizedstate%28%29.md)
  Get current quantized keys and values as tuples (efficient access)
- [func innerState() -> [MLXArray]](./quantizedkvcache/innerstate%28%29.md)
- [func toUnquantized() -> KVCacheSimple](./quantizedkvcache/tounquantized%28%29.md)
  Convert to unquantized cache
- [func trim(Int) -> Int](./quantizedkvcache/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./quantizedkvcache/update%28keys,values%29.md)
  This method is required by the KVCache protocol, but it is not intended to be used with QuantizedKVCache. Use `updateQuantized` instead.
- [func updateQuantized(keys: MLXArray, values: MLXArray) -> ((MLXArray, MLXArray, MLXArray?), (MLXArray, MLXArray, MLXArray?))](./quantizedkvcache/updatequantized%28keys,values%29.md)
  Update cache and return quantized tuples (Python’s update_and_fetch) This is needed because `update` in Swift must return `(MLXArray, MLXArray)`
### Type Properties
- [class var serializedClassName: String?](./quantizedkvcache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./quantizedkvcache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [BaseKVCache](./basekvcache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable
- [QuantizedKVCacheProtocol](./quantizedkvcacheprotocol.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcache)*