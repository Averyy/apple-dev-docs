---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmaxpolicy/limit(baseline:activesizes:)"
framework: "mlx-swift/MLX"
---

# limit(baseline:activeSizes:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Compute the desired wired limit in bytes for the current active set.

## Declaration

```swift
func limit(baseline: Int, activeSizes: [Int]) -> Int
```

#### Discussion

This is called after admission succeeds, whenever the manager needs to update the process-wide wired limit. The manager groups tickets by policy, calls this method with the sizes for that policy, then takes the maximum limit across all policies.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmaxpolicy/limit(baseline:activesizes:))*