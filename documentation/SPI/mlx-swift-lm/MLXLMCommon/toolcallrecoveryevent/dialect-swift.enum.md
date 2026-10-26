---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoveryevent/dialect-swift.enum"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallRecoveryEvent.Dialect

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

The textual dialect the model actually emitted.

## Declaration

```swift
enum Dialect
```

## Topics

### Enumeration Cases
- [ToolCallRecoveryEvent.Dialect.declaredArgs](./dialect-swift.enum/declaredargs.md)
  Markerless `name[ARGS]{...}` rehearsal syntax (promoted only under [`ToolCallRecoveryPolicy.permissive`](../toolcallrecoverypolicy/permissive.md)).
- [ToolCallRecoveryEvent.Dialect.gemma4](./dialect-swift.enum/gemma4.md)
  `<|tool_call>call:name{...}<tool_call|>`.
- [ToolCallRecoveryEvent.Dialect.mistral](./dialect-swift.enum/mistral.md)
  `[TOOL_CALLS]name[ARGS]{...}`.
- [ToolCallRecoveryEvent.Dialect.qwenFunction](./dialect-swift.enum/qwenfunction.md)
  `<function=name><parameter=k>v</parameter></function>`.
- [ToolCallRecoveryEvent.Dialect.toolCallFrame](./dialect-swift.enum/toolcallframe.md)
  `<tool_call>{...}</tool_call>` or `<tool_call><function=...>...</tool_call>`.
### Initializers
- [init?(rawValue: String)](./dialect-swift.enum/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./dialect-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](./dialect-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoveryevent/dialect-swift.enum)*