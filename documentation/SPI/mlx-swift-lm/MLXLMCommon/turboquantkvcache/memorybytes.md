---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/memorybytes"
framework: "mlx-swift-lm/MLXLMCommon"
---

# memoryBytes

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Actual memory footprint: compressed storage (packed indices + norms) for K and V, plus any raw FP16 buffers if still in prefill phase or rawKeyMode. Does NOT include codec overhead (rotation matrices, codebooks) which is shared across layers. In rawKeyMode: rawKeys is always present (FP16 keys), no keyPackedMSE/keyNorms.

## Declaration

```swift
var memoryBytes: Int { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/memorybytes)*