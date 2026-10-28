---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wired-memory"
framework: "mlx-swift/MLX"
---

# Wired Memory Management

**Framework**: mlx-swift/MLX  
**Role**: Article

Coordinate a process-wide wired memory limit for GPU workloads.

## Overview

Wired memory is a global process setting. MLX exposes a coordinator that lets multiple concurrent tasks agree on a single wired limit while still allowing different policies to coexist. The core types are:

- [`WiredMemoryManager`](./wiredmemorymanager.md): a coordinator that serializes updates and restores the baseline when work completes.
- [`WiredMemoryPolicy`](./wiredmemorypolicy.md): a policy interface that computes a desired limit and optionally gates admission.
- [`WiredMemoryTicket`](./wiredmemoryticket.md): a handle representing a unit of memory demand.

MLX provides generic policies such as `WiredSumPolicy` and `WiredMaxPolicy`. MLXLMCommon (from mlx-swift-lm) provides LLM-focused policies such as `WiredFixedPolicy`. You can use `GPU.maxRecommendedWorkingSetBytes()` as a portable upper bound when designing custom policies.

## Tickets and Work Types

Tickets represent memory demand. They come in two flavors:

- **Active** (`kind: .active`): indicates real work (e.g. inference). Active tickets drive limit updates.
- **Reservation** (`kind: .reservation`): represents long-lived memory such as model weights. Reservations participate in admission and limit computation, but do not keep the wired limit elevated while idle.

This lets you account for weights without leaving the wired limit high when no work is running.

## Policies and Grouping

Policies are grouped by their `id`. The manager computes one limit per policy group and then applies the **maximum** across groups. This prevents double-counting and allows heterogeneous strategies to coexist.

If you use reference-type policies, provide a stable `id` so grouping behaves as expected. Hashable value policies get an `id` automatically.

## Hysteresis

The manager applies hysteresis to avoid rapid shrink oscillations while active work is running:

- **Threshold**: a minimum fractional drop required before shrinking.
- **Cooldown**: a minimum time between shrink attempts.

Growing the limit is always allowed. These settings are configured with [`WiredMemoryManagerConfiguration`](./wiredmemorymanagerconfiguration.md).

## Debug Events

In DEBUG builds, `WiredMemoryManager.events()` emits a stream of [`WiredMemoryEvent`](./wiredmemoryevent.md) values describing admission and limit updates. In release builds, the stream finishes immediately and produces no events.

## Example

The following example uses a custom policy and demonstrates both reservation and active tickets:

```swift
struct SumPolicy: WiredMemoryPolicy, Hashable {
    func limit(baseline: Int, activeSizes: [Int]) -> Int {
        baseline + activeSizes.reduce(0, +)
    }
}

let policy = SumPolicy()

// Reserve model weights without keeping the limit elevated while idle.
let weights = policy.ticket(size: weightsBytes, kind: .reservation)
_ = await weights.start()

// Raise the limit only while inference is active.
let ticket = policy.ticket(size: kvBytes, kind: .active)
try await ticket.withWiredLimit {
    // run inference
}
```

## Admission Control

Policies can gate concurrency by implementing `canAdmit`. If admission fails, `start()` suspends until capacity becomes available. This is useful for preventing over-commit when many inferences launch simultaneously.

## Best Practices

- Use the shared manager (`WiredMemoryManager.shared`) unless you have a specific reason to isolate coordination (e.g. tests via `WiredMemoryManager.makeForTesting()`).
- Keep reservation tickets alive for the lifetime of a model or context.
- Prefer `withWiredLimit` to ensure cancellation-safe start/end pairing.
- Treat the manager as the sole authority for wired limit changes; external calls to `mlx_set_wired_limit` are undefined and may desynchronize the cached baseline.

## Policy-only mode (CPU or unsupported backends)

On systems where wired memory control is unavailable, you can still use the manager for **admission gating and budgeting** by enabling policy-only mode. In this mode the manager continues to track tickets and compute limits, but it does not attempt to change the process wired limit. Policy-only mode defaults to `true` on unsupported backends.

```swift
await WiredMemoryManager.shared.updateConfiguration { configuration in
    configuration.policyOnlyWhenUnsupported = true
}
```

### Choosing a baseline

When wired memory is unsupported, the manager will use:

1. `baselineOverride` if provided
2. `GPU.maxRecommendedWorkingSetBytes()` if available (default)
3. `0` as a fallback

This allows Apple Silicon CPU-only workloads to reuse the Metal recommended working set as a reasonable budget when unified memory is in play. The baseline is used for admission math only and does not change any OS limit.

## See Also

### MLX
- [Installation](./install.md)
  How to install and use.
- [Troubleshooting](./troubleshooting.md)
  Help with problems you might run into.
- [MLX Swift Examples](./examples.md)
  Swift example code for MLX and MLXNN.
- [Converting From Python](./converting-python.md)
  Common patterns from python and mapping `mlx` function names.
- [Numpy Style Broadcasting](./broadcasting.md)
  How different size arrays can be used together.
- [Lazy Evaluation](./lazy-evaluation.md)
  Computation in `MLX` is lazy.  Understand when the graph is evaluated.
- [Unified Memory](./unified-memory.md)
  `MLX` takes advantage of the shared memory between the CPU and GPU.
- [Vectorization](./vmap.md)
  Automatic vectorization with `vmap`.
- [Compilation](./compilation.md)
  MLX has a [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) function transformation which compiles computation graphs. Function compilation results in smaller graphs by merging common work and fusing certain operations. In many cases this can lead to big improvements in run-time and memory use.
- [Using Streams](./using-streams.md)
  Controlling where your computations are evaluated.
- [Running on iOS](./running-on-ios.md)
  Considerations for running on iOS and general memory tuning.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wired-memory)*