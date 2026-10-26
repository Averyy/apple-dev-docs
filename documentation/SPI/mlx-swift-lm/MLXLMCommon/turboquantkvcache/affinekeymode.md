---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/affinekeymode"
framework: "mlx-swift-lm/MLXLMCommon"
---

# affineKeyMode

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Affine-K mode: keys stored as 8-bit affine-quantized (upstream QuantizedKVCache layout, groupSize 64) while values are TurboQuant compressed. The efficient K per the asymmetric-kv paper: near-lossless like FP16 keys at half the bytes. Enabled when keyBits == 8.

## Declaration

```swift
let affineKeyMode: Bool
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/affinekeymode)*