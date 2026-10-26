---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpsharedkvsourceindiceskey"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mtpSharedKVSourceIndicesKey

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: var  
**Role**: Global Variable

Which cache entry each [`mtpSharedKVStatesKey`](./mtpsharedkvstateskey.md) tuple was read from, keyed the same way.

## Declaration

```swift
let mtpSharedKVSourceIndicesKey: LMOutput.Key<[String : Int]>
```

#### Discussion

A speculative round keeps only part of what its verify pass wrote, so the emitted snapshot has to be reconciled against the cache afterwards. That reconciliation is exact only if the consumer knows the entry behind each tuple: a sliding layer’s snapshot is bounded by its ring and a global layer’s is not, and at the crossing the two are indistinguishable by length.

Public alongside its siblings, because it is part of the same contract rather than an implementation detail of one writer: a target that sets [`mtpSharedKVStatesKey`](./mtpsharedkvstateskey.md) is expected to set this too, and a snapshot that arrives without it is refused rather than reconciled against a guessed bound. A target outside this package cannot satisfy that contract without it.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpsharedkvsourceindiceskey)*