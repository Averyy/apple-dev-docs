---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/gemma4sharedkvstate"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Gemma4SharedKVState

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Per-layer key/value state threaded between Gemma 4 decoder layers when KV sharing is enabled.

## Declaration

```swift
enum Gemma4SharedKVState
```

## Overview

`public` rather than `package` because `Gemma4DecoderLayer.callAsFunction` is exposed at `@_spi(GemmaEncoder)` scope for encoder-style client taps, and it appears in that signature — an SPI method cannot be called from outside the package if a type in its signature is package-scoped. Clients that do not use KV sharing pass `nil` and ignore the returned value.

## Topics

### Enumeration Cases
- [case quantized(keys: (MLXArray, MLXArray, MLXArray?), values: (MLXArray, MLXArray, MLXArray?), groupSize: Int, bits: Int, mode: QuantizationMode)](./gemma4sharedkvstate/quantized%28keys,values,groupsize,bits,mode%29.md)
- [case regular(keys: MLXArray, values: MLXArray)](./gemma4sharedkvstate/regular%28keys,values%29.md)
### Instance Properties
- [var sequenceLength: Int](./gemma4sharedkvstate/sequencelength.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/gemma4sharedkvstate)*