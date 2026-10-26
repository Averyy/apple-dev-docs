---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoveryevent/repair-swift.enum"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallRecoveryEvent.Repair

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

The repair applied to make the call executable.

## Declaration

```swift
enum Repair
```

## Topics

### Enumeration Cases
- [ToolCallRecoveryEvent.Repair.alternateDialect](./repair-swift.enum/alternatedialect.md)
  The payload was structurally complete as emitted; only the dialect differed from the selected format.
- [ToolCallRecoveryEvent.Repair.missingOuterClose](./repair-swift.enum/missingouterclose.md)
  The outer closing marker was missing at end of stream and the structurally complete payload was committed (permissive policy).
### Initializers
- [init?(rawValue: String)](./repair-swift.enum/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./repair-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](./repair-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoveryevent/repair-swift.enum)*