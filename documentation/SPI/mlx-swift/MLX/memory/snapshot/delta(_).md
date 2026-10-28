---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/snapshot/delta(_:)"
framework: "mlx-swift/MLX"
---

# delta(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Compute the difference between two snapshots:

## Declaration

```swift
func delta(_ other: Memory.Snapshot) -> Memory.Snapshot
```

## Discussion

```swift
let startMemory = Memory.snapshot()
...
let endMemory = Memory.snapshot()
print(startMemory.delta(endMemory))
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/memory/snapshot/delta(_:))*