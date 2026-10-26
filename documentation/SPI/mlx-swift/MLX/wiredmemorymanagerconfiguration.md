---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanagerconfiguration"
framework: "mlx-swift/MLX"
---

# WiredMemoryManagerConfiguration

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Configuration knobs for `WiredMemoryManager` behavior.

## Declaration

```swift
struct WiredMemoryManagerConfiguration
```

## Mentions

- [Wired Memory Management](./wired-memory.md)

#### Overview

These settings implement hysteresis to prevent small or frequent shrinks while active work is running. Growing the limit is always allowed; shrinking is gated by a minimum drop and a minimum time between changes.

## Topics

### Initializers
- [init(shrinkThresholdRatio: Double, shrinkCooldown: TimeInterval, policyOnlyWhenUnsupported: Bool, baselineOverride: Int?, useRecommendedWorkingSetWhenUnsupported: Bool)](./wiredmemorymanagerconfiguration/init%28shrinkthresholdratio,shrinkcooldown,policyonlywhenunsupported,baselineoverride,userecommendedworkingsetwhenunsupported%29.md)
  Creates a new configuration for hysteresis behavior.
### Instance Properties
- [var baselineOverride: Int?](./wiredmemorymanagerconfiguration/baselineoverride.md)
  Optional baseline to use instead of the cached limit. This is useful in policy-only mode to provide a meaningful budget.
- [var policyOnlyWhenUnsupported: Bool](./wiredmemorymanagerconfiguration/policyonlywhenunsupported.md)
  If true, policy admission and limit calculations still run even when wired memory control is unsupported (e.g. CPU-only execution). The manager will not attempt to change wired memory, but tickets can still gate admission and emit events. Defaults to `true` to keep admission behavior consistent across CPU/GPU backends.
- [var shrinkCooldown: TimeInterval](./wiredmemorymanagerconfiguration/shrinkcooldown.md)
  Minimum time in seconds between shrink attempts while tickets are active.
- [var shrinkThresholdRatio: Double](./wiredmemorymanagerconfiguration/shrinkthresholdratio.md)
  Minimum fractional drop required before shrinking while tickets are active. Example: 0.25 means the desired limit must be at least 25% lower than current.
- [var useRecommendedWorkingSetWhenUnsupported: Bool](./wiredmemorymanagerconfiguration/userecommendedworkingsetwhenunsupported.md)
  If true and wired memory is unsupported, attempt to use Metal’s recommended working set size as the baseline when no override is set.
### Default Implementations
- [Equatable Implementations](./wiredmemorymanagerconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanagerconfiguration)*