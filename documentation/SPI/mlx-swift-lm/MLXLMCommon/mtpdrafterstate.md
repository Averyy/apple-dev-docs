---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdrafterstate"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPDrafterState

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Per-stream state for MTP drafters that need their own transient storage.

## Declaration

```swift
struct MTPDrafterState
```

## Overview

The state is intentionally separate from [`LMOutput.State`](./lmoutput/state-swift.struct.md): `LMOutput` belongs to the target model’s step output, while this value is owned by the MTP iterator and passed only to the drafter.

## Topics

### Initializers
- [init(cache: [KVCache], nextPosition: Int, seedToken: MLXArray?, seedHidden: MLXArray?, proposalAppended: Int)](./mtpdrafterstate/init%28cache,nextposition,seedtoken,seedhidden,proposalappended%29.md)
### Instance Properties
- [var cache: [KVCache]](./mtpdrafterstate/cache.md)
- [var nextPosition: Int](./mtpdrafterstate/nextposition.md)
  Absolute next position in a drafter-owned autoregressive cache.
- [var proposalAppended: Int](./mtpdrafterstate/proposalappended.md)
  Number of tentative cache entries appended by the current proposal.
- [var seedHidden: MLXArray?](./mtpdrafterstate/seedhidden.md)
- [var seedToken: MLXArray?](./mtpdrafterstate/seedtoken.md)
  A proposal already computed while committing the previous verified round. Qwen uses this to avoid advancing its cache twice.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdrafterstate)*