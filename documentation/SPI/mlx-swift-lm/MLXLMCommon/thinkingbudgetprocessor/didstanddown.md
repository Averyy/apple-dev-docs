---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor/didstanddown"
framework: "mlx-swift-lm/MLXLMCommon"
---

# didStandDown

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Whether the processor stood down because a sampled token did not match the constraint it had applied.

## Declaration

```swift
var didStandDown: Bool { get }
```

## Discussion

That happens when another component overrides this one, or when the tokenizer disagrees with the model vocabulary. Standing down is the correct conservative response — the budget stops interfering and the model finishes under its own control — so this is a diagnostic, not an error. It is deliberately not a trap: a `precondition` here would crash a shipping generation loop, and an `assertionFailure` would crash debug builds of client apps.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor/didstanddown)*