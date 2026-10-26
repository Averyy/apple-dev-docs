---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanagerconfiguration/init(shrinkthresholdratio:shrinkcooldown:policyonlywhenunsupported:baselineoverride:userecommendedworkingsetwhenunsupported:)"
framework: "mlx-swift/MLX"
---

# init(shrinkThresholdRatio:shrinkCooldown:policyOnlyWhenUnsupported:baselineOverride:useRecommendedWorkingSetWhenUnsupported:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Creates a new configuration for hysteresis behavior.

## Declaration

```swift
init(shrinkThresholdRatio: Double = 0.25, shrinkCooldown: TimeInterval = 1.0, policyOnlyWhenUnsupported: Bool = true, baselineOverride: Int? = nil, useRecommendedWorkingSetWhenUnsupported: Bool = true)
```

## Parameters

- `shrinkThresholdRatio`: Minimum fractional drop to allow shrinking.
- `shrinkCooldown`: Minimum time between shrink attempts while active.
- `policyOnlyWhenUnsupported`: If true, policy admission and limit calculations still run even when wired memory control is unsupported.
- `baselineOverride`: Optional baseline to use instead of the cached limit.
- `useRecommendedWorkingSetWhenUnsupported`: If true and wired memory is unsupported, attempt to use Metal’s recommended working set size as the baseline.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanagerconfiguration/init(shrinkthresholdratio:shrinkcooldown:policyonlywhenunsupported:baselineoverride:userecommendedworkingsetwhenunsupported:))*