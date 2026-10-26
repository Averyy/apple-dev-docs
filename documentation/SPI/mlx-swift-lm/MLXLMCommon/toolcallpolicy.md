---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallpolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Rules for recovering and validating generated tool calls. Native parser requirements and declared-tool authorization always apply.

## Declaration

```swift
struct ToolCallPolicy
```

## Topics

### Initializers
- [init(recovery: ToolCallRecoveryPolicy, validation: ToolCallValidationPolicy)](./toolcallpolicy/init%28recovery,validation%29.md)
### Instance Properties
- [var recovery: ToolCallRecoveryPolicy](./toolcallpolicy/recovery.md)
  Bounded recovery of calls emitted in a different dialect. Applies to text formats; framed token protocols use their native parser.
- [var validation: ToolCallValidationPolicy](./toolcallpolicy/validation.md)
  Schema enforcement after unambiguous argument normalization.
### Default Implementations
- [Equatable Implementations](./toolcallpolicy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallpolicy)*