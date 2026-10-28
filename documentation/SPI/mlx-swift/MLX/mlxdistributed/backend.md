---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/backend"
framework: "mlx-swift/MLX"
---

# MLXDistributed.Backend

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

A communication backend.

## Declaration

```swift
enum Backend
```

## Overview

Use [`isAvailable(_:)`](./isavailable%28_%29.md) to check whether MLX was built with support for a given backend.  Note that availability means MLX can instantiate the backend, not that a communication group can actually be formed – use [`initialize(backend:strict:)`](./initialize%28backend,strict%29.md) with `strict: true` for that.

## Topics

### Enumeration Cases
- [MLXDistributed.Backend.any](./backend/any.md)
  Select the first available backend.
- [MLXDistributed.Backend.jaccl](./backend/jaccl.md)
- [MLXDistributed.Backend.mpi](./backend/mpi.md)
- [MLXDistributed.Backend.nccl](./backend/nccl.md)
- [MLXDistributed.Backend.ring](./backend/ring.md)
### Initializers
- [init?(rawValue: String)](./backend/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./backend/equatable-implementations.md)
- [RawRepresentable Implementations](./backend/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/backend)*