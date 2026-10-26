---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredbudgetpolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WiredBudgetPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Budget policy: `baseline + baseBytes + sum(activeSizes)`, optionally capped.

## Declaration

```swift
struct WiredBudgetPolicy
```

#### Overview

This policy is useful when you want to bake a learned or precomputed budget (for example, weights + workspace) into the limit calculation while still accounting for active tickets.

> **Note**: Pass a stable `id` if you intend to recreate the policy and keep it grouped with existing tickets.

##### Example

```swift
let base = weightsBytes + workspaceBytes
let policy = WiredBudgetPolicy(baseBytes: base)
let ticket = policy.ticket(size: kvBytes, kind: .active)
try await ticket.withWiredLimit {
    // run inference
}
```

## Topics

### Operators
- [static func == (WiredBudgetPolicy, WiredBudgetPolicy) -> Bool](./wiredbudgetpolicy/eqeq%28_,_%29.md)
### Initializers
- [init(baseBytes: Int, cap: Int?, id: UUID)](./wiredbudgetpolicy/init%28basebytes,cap,id%29.md)
  Creates a budget policy with an optional cap and stable id.
### Instance Properties
- [let baseBytes: Int](./wiredbudgetpolicy/basebytes.md)
  Base budget in bytes (e.g. weights + workspace).
- [let cap: Int?](./wiredbudgetpolicy/cap.md)
  Optional absolute cap (bytes) for the computed limit.
- [let identifier: UUID](./wiredbudgetpolicy/identifier.md)
  Stable policy identifier used for grouping.
### Instance Methods
- [func canAdmit(baseline: Int, activeSizes: [Int], newSize: Int) -> Bool](./wiredbudgetpolicy/canadmit%28baseline,activesizes,newsize%29.md)
  Admission is denied if the projected limit would exceed the cap.
- [func hash(into: inout Hasher)](./wiredbudgetpolicy/hash%28into%29.md)
- [func limit(baseline: Int, activeSizes: [Int]) -> Int](./wiredbudgetpolicy/limit%28baseline,activesizes%29.md)
  Computes the desired limit for the current active set.
### Default Implementations
- [Equatable Implementations](./wiredbudgetpolicy/equatable-implementations.md)
- [WiredMemoryPolicy Implementations](./wiredbudgetpolicy/wiredmemorypolicy-implementations.md)

## Relationships

### Conforms To
- MLX.WiredMemoryPolicy
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredbudgetpolicy)*