---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gptossmodel/toolcallformat"
framework: "mlx-swift-lm/MLXLLM"
---

# toolCallFormat

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: property  
**Role**: Instance Property

Selects the Harmony streaming path in the generation token loop.

## Declaration

```swift
var toolCallFormat: ToolCallFormat? { get }
```

#### Discussion

`.gptOSS` is not “another tool-call JSON dialect” — it means the full Harmony framing protocol (channels, recipients, terminators). The `ToolCallFormat` enum is the existing selection knob on `ChatConventionsProviding`; the implementation lives in `HarmonyFrameParser` / `HarmonyOutputRouter`.

Developer-provided `functions.*` calls are supported. Harmony’s built-in `browser.*` and `python` tools are intentionally not exposed or dispatched by this model integration.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gptossmodel/toolcallformat)*