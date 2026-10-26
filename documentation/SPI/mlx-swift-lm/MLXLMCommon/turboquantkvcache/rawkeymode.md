---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/rawkeymode"
framework: "mlx-swift-lm/MLXLMCommon"
---

# rawKeyMode

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Raw-K mode: keys stay at FP16 (uncompressed) while only values are TurboQuant compressed. This is the single biggest quality finding from TurboQuant+, K precision dominates quality via softmax amplification, V compression is nearly free (linear averaging). Enabled when keyBits == 0.

## Declaration

```swift
let rawKeyMode: Bool
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/rawkeymode)*