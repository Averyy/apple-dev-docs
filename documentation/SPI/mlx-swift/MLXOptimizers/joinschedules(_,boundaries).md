---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/joinschedules(_:boundaries:)"
framework: "mlx-swift/MLXOptimizers"
---

# joinSchedules(_:boundaries:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: func  
**Role**: Function

Join multiple schedules into one. Schedule `i + 1` receives a step count indicating the number of steps since the `i`-th boundary.

## Declaration

```swift
func joinSchedules(_ schedules: [(Int) -> Float], boundaries: [Int]) -> (Int) -> Float
```

## Parameters

- `schedules`: The schedules to join
- `boundaries`: `schedules.count - 1` step counts marking transitions


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/joinschedules(_:boundaries:))*