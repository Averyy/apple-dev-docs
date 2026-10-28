---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/group/split(color:key:)"
framework: "mlx-swift/MLX"
---

# split(color:key:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Split the group into subgroups based on the provided color.

## Declaration

```swift
func split(color: Int, key: Int = -1) throws -> MLXDistributed.Group
```

## Return Value

The subgroup this process belongs to

## Discussion

Processes that use the same color go to the same group.  The `key` argument defines the rank in the new group – the smaller the key the smaller the rank.  If the key is negative the rank in the current group is used.

Throws if the group cannot be split.  The ring and JACCL backends do not support splitting, and neither does a group of size one.

## Parameters

- `color`: A value to group processes into subgroups
- `key`: A key to optionally change the rank ordering of the processes


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/group/split(color:key:))*