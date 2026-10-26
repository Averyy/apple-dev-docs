---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallvalidationpolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallValidationPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Controls schema enforcement independently of syntax recovery and tool-name authorization. Both modes normalize unambiguous, schema-declared values.

## Declaration

```swift
enum ToolCallValidationPolicy
```

## Topics

### Enumeration Cases
- [ToolCallValidationPolicy.permissive](./toolcallvalidationpolicy/permissive.md)
  Forward parsed arguments after normalization, even if they violate the schema. This is the default; applications validate arguments themselves. Native parser requirements and declared-tool authorization still apply.
- [ToolCallValidationPolicy.strict](./toolcallvalidationpolicy/strict.md)
  Reject proven schema violations. Unsupported schema assertions remain unknown. Enable this to check arguments before automatic tool dispatch.
### Initializers
- [init?(rawValue: String)](./toolcallvalidationpolicy/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./toolcallvalidationpolicy/equatable-implementations.md)
- [RawRepresentable Implementations](./toolcallvalidationpolicy/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallvalidationpolicy)*