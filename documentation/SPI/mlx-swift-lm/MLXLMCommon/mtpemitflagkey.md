---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpemitflagkey"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mtpEmitFlagKey

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: var  
**Role**: Global Variable

The MTP iterator sets this key on the [`LMOutput.State`](./lmoutput/state-swift.struct.md) it passes into the main model on each call to opt the target into emitting [`mtpLastHiddenStatesKey`](./mtplasthiddenstateskey.md) and [`mtpSharedKVStatesKey`](./mtpsharedkvstateskey.md). An absent key reads as `false` (no emit), so non-MTP callers are unaffected.

## Declaration

```swift
let mtpEmitFlagKey: LMOutput.Key<Bool>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpemitflagkey)*