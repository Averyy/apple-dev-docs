---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoverypolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallRecoveryPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Policy governing bounded cross-dialect tool-call recovery.

## Declaration

```swift
enum ToolCallRecoveryPolicy
```

#### Overview

The selected `ToolCallFormat` parser is always authoritative. Recovery is a secondary pass that may promote a call written in a *different* common dialect when the model drifts from the selected one. Because recovery turns response text into executable actions, it is deliberately conservative: a missed recovery is preferable to a false execution.

## Topics

### Enumeration Cases
- [ToolCallRecoveryPolicy.conservative](./toolcallrecoverypolicy/conservative.md)
  Recover only structurally complete alternate-dialect calls that carry an explicit protocol marker (`<tool_call>`, `<|tool_call>`, `<function=`, `[TOOL_CALLS]`) and appear in committed response text — never inside reasoning spans (`<think>`/`<thinking>`/`[THINK]`), Markdown code spans or fences, or ordinary JSON data — and only when the call names an exactly declared tool. Argument normalization and schema enforcement are governed independently by [`ToolCallValidationPolicy`](./toolcallvalidationpolicy.md).
- [ToolCallRecoveryPolicy.disabled](./toolcallrecoverypolicy/disabled.md)
  Only the selected parser may produce calls. No alternate-dialect recovery is attempted.
- [ToolCallRecoveryPolicy.permissive](./toolcallrecoverypolicy/permissive.md)
  Everything [`ToolCallRecoveryPolicy.conservative`](./toolcallrecoverypolicy/conservative.md) does, plus promotion of exact markerless `declaredTool[ARGS]{...}` rehearsals in committed response text, and documented end-of-stream repair of calls whose outer closing marker is missing while their payload is structurally complete. Every promotion and repair is recorded in [`recoveryEvents`](./toolcallprocessor/recoveryevents.md) with its provenance. Markerless candidates that fail validation remain response text.
### Initializers
- [init?(rawValue: String)](./toolcallrecoverypolicy/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./toolcallrecoverypolicy/equatable-implementations.md)
- [RawRepresentable Implementations](./toolcallrecoverypolicy/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoverypolicy)*