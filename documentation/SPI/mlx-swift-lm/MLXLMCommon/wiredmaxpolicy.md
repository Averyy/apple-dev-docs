---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmaxpolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WiredMaxPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Max policy: `max(baseline, max(activeSizes))`.

## Declaration

```swift
struct WiredMaxPolicy
```

## Overview

This policy tracks the single largest active ticket. It is useful when you want the limit to scale with the largest in-flight request rather than the sum of concurrent work.

### Example

```swift
let policy = WiredMaxPolicy()
let ticket = policy.ticket(size: kvBytes, kind: .active)
try await ticket.withWiredLimit {
    // run inference
}
```

## Topics

### Initializers
- [init()](./wiredmaxpolicy/init%28%29.md)
  Creates a max policy.
### Instance Methods
- [func limit(baseline: Int, activeSizes: [Int]) -> Int](./wiredmaxpolicy/limit%28baseline,activesizes%29.md)
  Computes the desired limit for the current active set.
### Default Implementations
- [Equatable Implementations](./wiredmaxpolicy/equatable-implementations.md)
- [WiredMemoryPolicy Implementations](./wiredmaxpolicy/wiredmemorypolicy-implementations.md)

## Relationships

### Conforms To
- MLX.WiredMemoryPolicy
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmaxpolicy)*