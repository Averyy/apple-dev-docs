---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loralayer/loraenabled"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loraEnabled

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

When false the layer behaves as the underlying base layer (no LoRA term added). Used by callers like `linearSpecGenerate` that need to toggle the adapter between draft and verify phases without unloading it.

## Declaration

```swift
var loraEnabled: Bool { get set }
```

## Discussion

A default implementation is provided so existing `LoRALayer` conformers continue to compile unchanged — they appear as non-toggleable (always-on) layers, and `setLoRAEnabled(_:)` is a no-op for them. The four built-in implementations (`LoRALinear`, `QLoRALinear`, `DoRALinear`, `QDoRALinear`) override this with a stored property to provide the real toggle.

## Default Implementations

### LoRALayer Implementations
- [var loraEnabled: Bool](./loraenabled-69oqf.md)
  Default no-op toggle. Returns true (LoRA always applied) and ignores writes. Concrete classes that want a real toggle override this with a stored property — see `LoRALinear` etc.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loralayer/loraenabled)*