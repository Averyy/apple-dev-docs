---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/group"
framework: "mlx-swift/MLX"
---

# MLXDistributed.Group

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

A group of independent MLX processes that can communicate.

## Declaration

```swift
final class Group
```

## Overview

Obtain a group with [`initialize(backend:strict:)`](./initialize%28backend,strict%29.md).

## Topics

### Instance Properties
- [var rank: Int](./group/rank.md)
  The rank of this process in the group.
- [var size: Int](./group/size.md)
  The number of processes in the group.
### Instance Methods
- [func split(color: Int, key: Int) throws -> MLXDistributed.Group](./group/split%28color,key%29.md)
  Split the group into subgroups based on the provided color.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/group)*