---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/hasclosedreasoning"
framework: "mlx-swift-lm/MLXLMCommon"
---

# hasClosedReasoning

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

True once a canonical or implicit end boundary has been observed, i.e. a reasoning span has closed at least once. Unlike [`isInsideReasoning`](./isinsidereasoning.md), this latches — so a caller (e.g. a think-then-call token collector) can detect a close even when an empty `<think></think>` resolves within a single [`process(_:)`](./process%28_%29.md) call, where sampling [`isInsideReasoning`](./isinsidereasoning.md) afterward reads `false` both before and after and the transient open is invisible.

## Declaration

```swift
var hasClosedReasoning: Bool { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/hasclosedreasoning)*