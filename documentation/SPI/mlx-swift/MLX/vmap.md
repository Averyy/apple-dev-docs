---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vmap"
framework: "mlx-swift/MLX"
---

# Vectorization

**Framework**: mlx-swift/MLX  
**Role**: Article

Automatic vectorization with `vmap`.

## Overview

`vmap` transforms a function so that it operates independently over a batch axis. This is convenient for evaluating a function over many inputs without writing explicit loops.

## Basics of vmap

Let’s start with a simple example:

```swift
func f(_ x: MLXArray) -> MLXArray { x * 2 }

let x = MLXArray(0 ..< 6, [3, 2])

let vf = vmap(f)
let y = vf(x)
```

This is equivalent to calling `f` on each slice of `x` along the first axis and stacking the results:

```swift
let manual = stacked((0 ..< 3).map { f(x[$0]) }, axis: 0)
```

Both approaches produce the same array.

The `inAxes` parameter controls which axis of each input to map over. Passing `nil` for an input disables mapping for that value. The `outAxes` parameter specifies the axis of each output where the batched results are stacked.

```swift
func add(_ x: MLXArray, _ y: MLXArray) -> MLXArray { x + y }
let vf = vmap(add, inAxes: (0, nil))
```

Here `x` is mapped over its first axis while `y` is used as a broadcast value.

## Nested Mapping

You can nest calls to `vmap` to map over multiple axes. Each nested `vmap` introduces another batch dimension in the result.

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
- [Compilation](./compilation.md)
  MLX has a [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) function transformation which compiles computation graphs. Function compilation results in smaller graphs by merging common work and fusing certain operations. In many cases this can lead to big improvements in run-time and memory use.
- [Using Streams](./using-streams.md)
  Controlling where your computations are evaluated.
- [Running on iOS](./running-on-ios.md)
  Considerations for running on iOS and general memory tuning.
- [Wired Memory Management](./wired-memory.md)
  Coordinate a process-wide wired memory limit for GPU workloads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vmap)*