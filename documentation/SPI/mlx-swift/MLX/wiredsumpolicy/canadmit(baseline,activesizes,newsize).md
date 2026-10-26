---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredsumpolicy/canadmit(baseline:activesizes:newsize:)"
framework: "mlx-swift/MLX"
---

# canAdmit(baseline:activeSizes:newSize:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Decide whether a new ticket can be admitted. Defaults to allowing all tickets.

## Declaration

```swift
func canAdmit(baseline: Int, activeSizes: [Int], newSize: Int) -> Bool
```

#### Discussion

This is evaluated before a ticket is started. If it returns false, `start()` will suspend until another ticket ends and capacity becomes available. Admission checks only consider tickets that share the same policy grouping.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredsumpolicy/canadmit(baseline:activesizes:newsize:))*