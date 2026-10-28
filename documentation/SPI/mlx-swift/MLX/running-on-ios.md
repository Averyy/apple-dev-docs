---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios"
framework: "mlx-swift/MLX"
---

# Running on iOS

**Framework**: mlx-swift/MLX  
**Role**: Article

Considerations for running on iOS and general memory tuning.

## Controlling Memory Use

iOS devices have a feature called [jetsam](https://developer.apple.com/documentation/xcode/identifying-high-memory-use-with-jetsam-event-reports) which will terminate processes if they use too much memory.

Models may take several gigabytes for their weights, and they need memory on top of that for evaluation.  The size of weights can be controlled by using narrower types, e.g. `Float16` instead of `Float32` or quantizing the weights with the [QuantizeLinear](../MLXNN/quantizedlinear.md) layer.

The LLM models in the [MLX Swift Examples](./examples.md) already make use of these techniques.

As MLX evaluates graphs (models), it produces temporary buffers and results. These are managed automatically, and for efficiency MLX will recycle the buffers after they are disposed. The limit on this cache is determined by Metal’s [recommendedMaxWorkingSetSize()](https://developer.apple.com/documentation/metal/mtldevice/2369280-recommendedmaxworkingsetsize), but you may wish to limit this further.

For example, to evaluate an LLM you might allow up to 20 megabytes of buffer cache via [`Memory`](./memory.md).

```swift
MLX.Memory.cacheLimit = 20 * 1024 * 1024
```

[`snapshot()`](./memory/snapshot%28%29.md) can be used to monitor memory use over time:

```swift
// load model & weights
...

let startMemory = Memory.snapshot()

// work
...

let endMemory = Memory.snapshot()

// what stats are interesting to you?

print("=======")
print("Memory size: \(Memory.memoryLimit / 1024)K")
print("Cache size:  \(Memory.cacheLimit / 1024)K")

print("")
print("=======")
print("Starting memory")
print(startMemory.description)

print("")
print("=======")
print("Ending memory")
print(endMemory.description)

print("")
print("=======")
print("Growth")
print(startMemory.delta(endMemory).description)
```

It may be interesting to print the current memory statistics during evaluation if you want to see performance over time.

Decreasing the cache limit to 0 will result in decreased performance due to the lack of buffer reuse, but it will also result in smaller memory use. Tune this value for your needs.

Finally, if the device your code runs on has more RAM than the jetsam limit would normally allow, you can use the [Increased Memory Limit](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_kernel_increased-memory-limit) entitlement.

## Developing for iOS

Typically developers use the [iOS simulator](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device/) to develop new iOS applications.  It gives you an easy way to configure different device types.

It isn’t possible to use the iOS simulator for developing MLX applications, since MLX requires a modern [Metal MTLGPUFamily](https://developer.apple.com/documentation/metal/mtlgpufamily) and the simulator does not provide that.

If you try to use the simulator, you may encounter error messages like this:

```
failed assertion `Dispatch Threads with Non-Uniform Threadgroup Size is not supported on this device'
```

This is an indication that it is trying to use an unsupported Metal feature.

Here are two recommended workarounds:

- Add the `Mac (Designed for iPad)` destination to your target in Xcode.

  - MLX requires Apple silicon, and this feature lets you build an iPad application that will run on macOS.
  - The UI may present with differences to iOS, but this will allow you to build an iOS binary that runs with a fully featured Metal GPU.
- Make a [multiplatform](https://developer.apple.com/documentation/xcode/configuring-a-multiplatform-app-target) application that can run on macOS, iOS and iPadOS.

  - With SwiftUI it is possible to do most of your development in a macOS application and fine tune it for iOS by running it on an actual device.

Of course you can also use the simulator for developing UI features, you just won’t be able to evaluate any [`MLXArray`](./mlxarray.md).

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
- [Wired Memory Management](./wired-memory.md)
  Coordinate a process-wide wired memory limit for GPU workloads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios)*