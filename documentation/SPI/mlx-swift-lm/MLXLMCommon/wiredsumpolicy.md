---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredsumpolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WiredSumPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Sum policy: `baseline + sum(activeSizes)`, optionally capped.

## Declaration

```swift
struct WiredSumPolicy
```

#### Overview

This is the most common policy for inference workloads. Each ticket adds to the wired limit, making the total proportional to concurrent demand.

If `cap` is nil, the policy clamps to `GPU.maxRecommendedWorkingSetBytes()` when available. If a cap is provided, both limit computation and admission respect it.

##### Example

```swift
let policy = WiredSumPolicy(cap: 12 * 1024 * 1024 * 1024)
let ticket = policy.ticket(size: kvBytes, kind: .active)
try await ticket.withWiredLimit {
    // run inference
}
```

## Topics

### Initializers
- [init(cap: Int?)](./wiredsumpolicy/init%28cap%29.md)
  Creates a sum policy with an optional cap in bytes.
### Instance Properties
- [let cap: Int?](./wiredsumpolicy/cap.md)
  Optional absolute cap (bytes) for the computed limit.
### Instance Methods
- [func canAdmit(baseline: Int, activeSizes: [Int], newSize: Int) -> Bool](./wiredsumpolicy/canadmit%28baseline,activesizes,newsize%29.md)
  Admission is denied if the projected limit would exceed the cap.
- [func limit(baseline: Int, activeSizes: [Int]) -> Int](./wiredsumpolicy/limit%28baseline,activesizes%29.md)
  Computes the desired limit for the current active set.
### Default Implementations
- [Equatable Implementations](./wiredsumpolicy/equatable-implementations.md)
- [WiredMemoryPolicy Implementations](./wiredsumpolicy/wiredmemorypolicy-implementations.md)

## Relationships

### Conforms To
- MLX.WiredMemoryPolicy
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredsumpolicy)*