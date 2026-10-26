---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorypolicy/canadmit(baseline:activesizes:newsize:)"
framework: "mlx-swift/MLX"
---

# canAdmit(baseline:activeSizes:newSize:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Decide whether a new ticket can be admitted. Defaults to allowing all tickets.

## Declaration

```swift
func canAdmit(baseline: Int, activeSizes: [Int], newSize: Int) -> Bool
```

#### Discussion

This is evaluated before a ticket is started. If it returns false, `start()` will suspend until another ticket ends and capacity becomes available. Admission checks only consider tickets that share the same policy grouping.

## Default Implementations

### WiredMemoryPolicy Implementations
- [func canAdmit(baseline: Int, activeSizes: [Int], newSize: Int) -> Bool](./canadmit%28baseline,activesizes,newsize%29-2qjzs.md)
  Decide whether a new ticket can be admitted. Defaults to allowing all tickets.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorypolicy/canadmit(baseline:activesizes:newsize:))*