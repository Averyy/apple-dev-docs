---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reranktruncationpolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RerankTruncationPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Controls how inputs that exceed a model’s context limit are handled.

## Declaration

```swift
enum RerankTruncationPolicy
```

## Topics

### Enumeration Cases
- [RerankTruncationPolicy.error](./reranktruncationpolicy/error.md)
  Reject an overlong input instead of truncating it.
- [RerankTruncationPolicy.truncate](./reranktruncationpolicy/truncate.md)
  Truncate model input content while preserving required structural prompt tokens.
### Default Implementations
- [Equatable Implementations](./reranktruncationpolicy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reranktruncationpolicy)*