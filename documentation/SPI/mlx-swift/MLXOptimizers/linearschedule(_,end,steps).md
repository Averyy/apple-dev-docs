---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/linearschedule(_:end:steps:)"
framework: "mlx-swift/MLXOptimizers"
---

# linearSchedule(_:end:steps:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: func  
**Role**: Function

Make a linear schedule from `initial` to `end` over `steps`. The value is `end` for any steps beyond `steps`.

## Declaration

```swift
func linearSchedule(_ initial: Float, end: Float, steps: Int) -> (Int) -> Float
```

## Parameters

- `initial`: Initial value
- `end`: Final value
- `steps`: Number of steps to apply the schedule over (must be >= 1)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/linearschedule(_:end:steps:))*