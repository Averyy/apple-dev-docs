---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/segments"
framework: "mlx-swift/MLXNN"
---

# Segments

**Framework**: mlx-swift/MLXNN  
**Kind**: enum  
**Role**: Enumeration

Describes how an unsharded weight is composed.

## Declaration

```swift
enum Segments
```

#### Overview

A fused QKV matrix, for example, is three segments stacked together and each has to be sharded separately.

## Topics

### Enumeration Cases
- [Segments.count(_:)](./segments/count%28_%29.md)
  The weight is `count` equally sized segments.
- [case fractions([Double])](./segments/fractions%28_%29.md)
  The weight is split at these fractions of the axis.
- [Segments.indices(_:)](./segments/indices%28_%29.md)
  The weight is split at these indices.
### Default Implementations
- [Equatable Implementations](./segments/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/segments)*