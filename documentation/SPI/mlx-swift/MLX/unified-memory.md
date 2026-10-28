---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/unified-memory"
framework: "mlx-swift/MLX"
---

# Unified Memory

**Framework**: mlx-swift/MLX  
**Role**: Article

`MLX` takes advantage of the shared memory between the CPU and GPU.

## Discussion

See also [mlx python docs](https://ml-explore.github.io/mlx/build/html/usage/unified_memory.html).

Apple silicon has a unified memory architecture. The CPU and GPU have direct access to the same memory pool. MLX is designed to take advantage of that.

Concretely, when you make an array in MLX you don’t have to specify its location:

```swift
let a = MLXRandom.normal([100])
let b = MLXRandom.normal([100])
```

Both `a` and `b` live in unified memory.

In MLX, rather than moving arrays to devices, you specify the device when you run the operation. Any device can perform any operation on `a` and `b` without needing to move them from one memory location to another. For example:

```swift
add(a, b, stream: .cpu)
add(a, b, stream: .gpu)
```

In the above, both the CPU and the GPU will perform the same add operation. The operations can (and likely will) be run in parallel since there are no dependencies between them. See [Using Streams](./using-streams.md) for more information the semantics of streams in MLX.

In the above `add` example, there are no dependencies between operations, so there is no possibility for race conditions. If there are dependencies, the MLX scheduler will automatically manage them. For example:

```swift
let c = add(a, b, stream: .cpu)
let d = add(a, c, stream: .gpu)
```

In the above case, the second `add` runs on the GPU but it depends on the output of the first `add` which is running on the CPU. MLX will automatically insert a dependency between the two streams so that the second `add` only starts executing after the first is complete and `c` is available.

## A Simple Example

Here is a more interesting (albeit slightly contrived example) of how unified memory can be helpful. Suppose we have the following computation:

```swift
func f(a: MLXArray, b: MLXArray, d1: StreamOrDevice, d2: StreamOrDevice) -> (MLXArray, MLXArray) {
    let x = matmul(a, b, stream: d1)
    var b = b
    for _ in 0 ..< 500 {
        b = exp(b, stream: d2)
    }
    return (x, b)
}
```

which we want to run with the following arguments:

```swift
let a = MLXRandom.uniform([4096, 512])
let b = MLXRandom.uniform([512, 4])
```

The first `matmul` operation is a good fit for the GPU since it’s more compute dense. The second sequence of operations are a better fit for the CPU, since they are very small and would probably be overhead bound on the GPU.

If we time the computation fully on the GPU, we get 2.8 milliseconds. But if we run the computation with `d1: .gpu` and `d2: .cpu`, then the time is only about 1.4 milliseconds, about twice as fast. These times were measured on an M1 Max.

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/unified-memory)*