---
source: mlx-swift
framework: MLX-Swift
url: https://github.com/ml-explore/mlx-swift/blob/main/Source/MLX/Documentation.docc/MLX.md
---

#  ``MLX``

MLX Swift is a Swift API for MLX.

MLX is an array framework for machine learning on Apple silicon. MLX Swift
expands MLX to the Swift language, making research and experimentation easier
on Apple silicon.

The Swift API closely follows the 
[C++ and Python MLX APIs](https://ml-explore.github.io/mlx/build/html/index.html), which in turn closely follow
NumPy with a few exceptions. Here are some useful pages showing how MLX Swift works and is different
from python:

- [Converting From Python](Articles/converting-python.md) -- information about converting Python code and differences between Python and Swift
- [Indexing](Organization/indexing.md) -- information about array indexing
- [Arithmetic](Organization/arithmetic.md) -- information about array arithmetic

The main differences between MLX and NumPy are:

 - **Composable function transformations**: MLX has composable function
   transformations for automatic differentiation, automatic vectorization,
   and computation graph optimization.
 - **[Lazy Evaluation](Articles/lazy-evaluation.md)**: Computations in MLX are lazy. Arrays are only
   materialized when needed.
 - **Multi-device**: Operations can run on any of the supported devices (CPU,
   GPU, ...)

The design of MLX is inspired by frameworks like 
[PyTorch](https://pytorch.org/), [Jax](https://github.com/google/jax), and
[ArrayFire](https://arrayfire.org/). A notable difference from these
frameworks and MLX is the [Unified Memory](Articles/unified-memory.md). Arrays in MLX live in shared
memory. Operations on MLX arrays can be performed on any of the supported
device types without performing data copies. Currently supported device types
are the CPU and GPU.

## Wired Memory

MLX includes a process-wide wired memory coordinator for GPU workloads. Use
`WiredMemoryManager` and `WiredMemoryTicket` to coordinate wired limit changes
across concurrent tasks, and implement `WiredMemoryPolicy` to define how limits
are computed.

MLX ships generic policies like `WiredSumPolicy` and `WiredMaxPolicy`. For
LLM-oriented defaults (such as fixed budgets or admission gating), see
MLXLMCommon in mlx-swift-lm.

Tickets can represent active work (`kind: .active`) or long-lived reservations
(`kind: .reservation`) so you can account for model weights without keeping the
wired limit elevated while idle.

```swift
let policy = WiredSumPolicy()

// Optional: reserve model weights without keeping the limit elevated while idle.
let weights = policy.ticket(size: weightsBytes, kind: .reservation)
_ = await weights.start()

// Raise the limit only while inference is active.
let ticket = policy.ticket(size: kvBytes, kind: .active)
try await ticket.withWiredLimit {
    // run inference
}
```

See [Wired Memory Management](Articles/wired-memory.md) for configuration, best practices, and policy guidance.

## Other MLX Packages

- [MLXNN](mlxnn)
- [MLXOptimizers](mlxoptimizers)

- [Python `mlx`](https://ml-explore.github.io/mlx/build/html/index.html)

## Topics

### MLX

- [Installation](install.md)
- [Troubleshooting](troubleshooting.md)
- [MLX Swift Examples](examples.md)
- [Converting From Python](Articles/converting-python.md)
- [Numpy Style Broadcasting](Articles/broadcasting.md)
- [Lazy Evaluation](Articles/lazy-evaluation.md)
- [Unified Memory](Articles/unified-memory.md)
- [Vectorization](Articles/vmap.md)
- [Compilation](Articles/compilation.md)
- [Using Streams](Articles/using-streams.md)
- [Running on iOS](Articles/running-on-ios.md)
- [Wired Memory Management](Articles/wired-memory.md)

### MLXArray

- ``MLXArray``

### Free Functions

- [Free Functions](free-functions.md)

### Memory

- ``GPU``
- ``WiredMemoryManager``
- ``WiredMemoryTicket``
- ``WiredMemoryPolicy``
- ``WiredMemoryEvent``

### Data Types

- ``DType``
- ``HasDType``
- ``ScalarOrArray``
- ``NestedArrayElement``

### Parameter Types

- ``IntOrPair``
- ``IntOrTriple``
- ``IntOrArray``
- ``FloatOrArray``

### Nested Data

- ``NestedDictionary``
- ``NestedItem``
- ``IndentedDescription``

### Streams and Devices

- ``StreamOrDevice``
- ``Device``
- ``DeviceType``
- ``Stream``

### Distributed

- ``MLXDistributed``
