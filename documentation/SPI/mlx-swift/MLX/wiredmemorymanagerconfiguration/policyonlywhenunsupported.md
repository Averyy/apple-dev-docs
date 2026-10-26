---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanagerconfiguration/policyonlywhenunsupported"
framework: "mlx-swift/MLX"
---

# policyOnlyWhenUnsupported

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

If true, policy admission and limit calculations still run even when wired memory control is unsupported (e.g. CPU-only execution). The manager will not attempt to change wired memory, but tickets can still gate admission and emit events. Defaults to `true` to keep admission behavior consistent across CPU/GPU backends.

## Declaration

```swift
var policyOnlyWhenUnsupported: Bool
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanagerconfiguration/policyonlywhenunsupported)*