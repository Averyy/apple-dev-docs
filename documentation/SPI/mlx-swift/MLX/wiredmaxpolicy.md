---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmaxpolicy"
framework: "mlx-swift/MLX"
---

# WiredMaxPolicy

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Policy that uses the maximum active ticket size and adds it to the baseline.

## Declaration

```swift
struct WiredMaxPolicy
```

## Topics

### Initializers
- [init(id: UUID)](./wiredmaxpolicy/init%28id%29.md)
### Instance Properties
- [let identifier: UUID](./wiredmaxpolicy/identifier.md)
  Stable grouping identifier for this policy instance.
### Instance Methods
- [func limit(baseline: Int, activeSizes: [Int]) -> Int](./wiredmaxpolicy/limit%28baseline,activesizes%29.md)
  Compute the desired wired limit in bytes for the current active set.
### Default Implementations
- [Equatable Implementations](./wiredmaxpolicy/equatable-implementations.md)
- [WiredMemoryPolicy Implementations](./wiredmaxpolicy/wiredmemorypolicy-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype
- [WiredMemoryPolicy](./wiredmemorypolicy.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmaxpolicy)*