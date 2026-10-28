---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/install"
framework: "mlx-swift/MLX"
---

# Installation

**Framework**: mlx-swift/MLX  
**Role**: Article

How to install and use.

## Overview

[MLX](./MLX.md) is meant to be built and run from Xcode or SwiftPM.

## Xcode

In Xcode you can add `https://github.com/ml-explore/mlx-swift` as a package dependency and link `MLX`, `MLXNN` and `MLXRandom` as needed.

## SwiftPM

To use [MLX](./MLX.md) with SwiftPm you can add this to your `Package.swift`:

```swift
dependencies: [
    .package(url: "https://github.com/ml-explore/mlx-swift", from: "0.10.0")
]
```

and add the libraries (as needed) as dependencies:

```swift
dependencies: [.product(name: "MLX", package: "mlx-swift"),
               .product(name: "MLXRandom", package: "mlx-swift"),
               .product(name: "MLXNN", package: "mlx-swift"),
               .product(name: "MLXOptimizers", package: "mlx-swift"),
               .product(name: "MLXFFT", package: "mlx-swift")]
```

> **Note**: Note that SwiftPM cannot build the metal shaders so the ultimate build has to be done via Xcode or `xcodebuild`.

## Command Line Tools

See [Troubleshooting](./troubleshooting.md) (Running From Command Line) for information about running command line tools from the shell.

## See Also

### MLX
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
- [Wired Memory Management](./wired-memory.md)
  Coordinate a process-wide wired memory limit for GPU workloads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/install)*