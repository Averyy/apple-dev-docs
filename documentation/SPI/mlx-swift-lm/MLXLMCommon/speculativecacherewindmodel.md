---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativecacherewindmodel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SpeculativeCacheRewindModel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Target-side capability for rewinding an in-place speculative verify pass.

## Declaration

```swift
protocol SpeculativeCacheRewindModel
```

## Overview

Rollback belongs to the target/cache implementation, not to the drafter. The depth is explicit so a future multi-token drafter cannot accidentally select an in-place path whose recurrent checkpoint is too shallow.

## Topics

### Instance Properties
- [var maximumNativeTargetCacheRewind: Int](./speculativecacherewindmodel/maximumnativetargetcacherewind.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativecacherewindmodel)*