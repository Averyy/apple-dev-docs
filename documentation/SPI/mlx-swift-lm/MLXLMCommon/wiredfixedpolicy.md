---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredfixedpolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WiredFixedPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Fixed policy: limit is constant while any ticket is active.

## Declaration

```swift
struct WiredFixedPolicy
```

#### Overview

This policy ignores the active sizes and applies a fixed limit any time at least one ticket is active. It is useful when you want a deterministic cap.

##### Example

```swift
let policy = WiredFixedPolicy(limit: 8 * 1024 * 1024 * 1024)
let ticket = policy.ticket(size: kvBytes, kind: .active)
try await ticket.withWiredLimit {
    // run inference
}
```

## Topics

### Initializers
- [init(limit: Int)](./wiredfixedpolicy/init%28limit%29.md)
  Creates a fixed policy with the given limit in bytes.
### Instance Properties
- [let bytes: Int](./wiredfixedpolicy/bytes.md)
  Fixed limit in bytes to apply while any ticket is active.
### Instance Methods
- [func limit(baseline: Int, activeSizes: [Int]) -> Int](./wiredfixedpolicy/limit%28baseline,activesizes%29.md)
  Computes the desired limit for the current active set.
### Default Implementations
- [Equatable Implementations](./wiredfixedpolicy/equatable-implementations.md)
- [WiredMemoryPolicy Implementations](./wiredfixedpolicy/wiredmemorypolicy-implementations.md)

## Relationships

### Conforms To
- MLX.WiredMemoryPolicy
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredfixedpolicy)*