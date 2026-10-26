---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatestopreason"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerateStopReason

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Reason why token generation stopped.

## Declaration

```swift
enum GenerateStopReason
```

## Topics

### Enumeration Cases
- [GenerateStopReason.cancelled](./generatestopreason/cancelled.md)
  Generation stopped due to explicit task cancellation or early stream termination.
- [GenerateStopReason.length](./generatestopreason/length.md)
  Generation stopped because the configured max token limit was reached.
- [GenerateStopReason.stop](./generatestopreason/stop.md)
  Generation stopped because an EOS/unknown stop token was encountered.
### Default Implementations
- [Equatable Implementations](./generatestopreason/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatestopreason)*