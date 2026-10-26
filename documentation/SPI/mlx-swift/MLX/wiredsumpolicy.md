---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredsumpolicy"
framework: "mlx-swift/MLX"
---

# WiredSumPolicy

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Policy that sums active ticket sizes and adds them to the baseline.

## Declaration

```swift
struct WiredSumPolicy
```

## Topics

### Initializers
- [init(id: UUID)](./wiredsumpolicy/init%28id%29.md)
### Instance Properties
- [let identifier: UUID](./wiredsumpolicy/identifier.md)
  Stable grouping identifier for this policy instance.
### Instance Methods
- [func limit(baseline: Int, activeSizes: [Int]) -> Int](./wiredsumpolicy/limit%28baseline,activesizes%29.md)
  Compute the desired wired limit in bytes for the current active set.
### Default Implementations
- [Equatable Implementations](./wiredsumpolicy/equatable-implementations.md)
- [WiredMemoryPolicy Implementations](./wiredsumpolicy/wiredmemorypolicy-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype
- [WiredMemoryPolicy](./wiredmemorypolicy.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredsumpolicy)*