---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/using-streams"
framework: "mlx-swift/MLX"
---

# Using Streams

**Framework**: mlx-swift/MLX  
**Role**: Article

Controlling where your computations are evaluated.

## Specifying the Stream

All operations, including random number generation, take an optional `stream:` argument. It defaults to [`defaultStream`](./stream/defaultstream.md) – the default stream of the default device.

For example:

```swift
// produced on the CPU
let a = uniform(0 ..< 1, [100, 100], stream: .cpu)

// produced on the GPU
let b = uniform(0 ..< 1, [100, 100], stream: .gpu)
```

The argument is a [`StreamOrDevice`](./streamordevice.md). [`cpu`](./streamordevice/cpu.md) and [`gpu`](./streamordevice/gpu.md) select whichever stream is currently in effect for that device, which the scopes below control.

## Scoping the Default Device

To avoid passing `stream:` to every call, change the default device for a scope. [`withDefaultDevice(_:_:)`](./device/withdefaultdevice%28_,_%29-17vjl.md) does this without creating any new streams:

```swift
Device.withDefaultDevice(.cpu) {
    // no stream: argument needed -- these run on the CPU
    let a = uniform(0 ..< 1, [100, 100])
    let b = uniform(0 ..< 1, [100, 100])
}
```

Inside the scope, [`defaultDevice()`](./device/defaultdevice%28%29.md) returns the CPU device and [`default`](./streamordevice/default.md) resolves to the CPU stream. On exit, the previous default is restored.

## Scoping a New Stream

[`withNewDefaultStream(device:_:)`](./stream/withnewdefaultstream%28device,_%29-5bwc3.md) sets the default device and creates *new* streams for the scope:

```swift
Stream.withNewDefaultStream(device: .cpu) {
    // a new stream, private to this scope
    let a = uniform(0 ..< 1, [100, 100])
}
```

Use this when work must be independent of the enclosing scope’s streams – for example so a [`synchronize()`](./stream/synchronize%28%29.md) waits only on your own work. Use [`withDefaultDevice(_:_:)`](./device/withdefaultdevice%28_,_%29-17vjl.md) when you only want to redirect work to a different device.

`withNewDefaultStream` replaces *both* the CPU and GPU streams for the scope, not only the one named by `device:`. Code inside that explicitly asks for the other device also gets a new stream:

```swift
Stream.withNewDefaultStream(device: .cpu) {
    // a new CPU stream -- and `stream: .gpu` here is also a new
    // stream, not the GPU stream from the enclosing scope
    let a = uniform(0 ..< 1, [100, 100], stream: .gpu)
}
```

This does not affect correctness: MLX inserts dependencies between streams automatically, as described in [Unified Memory](./unified-memory.md).

Both calls nest arbitrarily, and both have `async` variants.

## Propagating Scopes Across Tasks

These scopes are task-local. They are inherited by `async let` and by child tasks of a `TaskGroup`:

```swift
await Device.withDefaultDevice(.cpu) {
    await withTaskGroup(of: Void.self) { group in
        group.addTask {
            // still the CPU
            let a = uniform(0 ..< 1, [100, 100])
        }
    }
}
```

They are *not* inherited by `Task.detached` or by a `Thread`, which see the process-wide default instead. Work started that way must establish its own scope:

```swift
Task.detached {
    Device.withDefaultDevice(.cpu) {
        // the scope has to be re-established here
    }
}
```

## Holding a Stream Directly

When a stream must outlive a single scope, create a [`Stream`](./stream.md) and pass it explicitly:

```swift
let stream = Stream(Device(.cpu))
let a = uniform(0 ..< 1, [100, 100], stream: .stream(stream))
```

Streams are pooled: the underlying resources are recycled when the `Stream` is released, so creating them in a loop does not exhaust system resources. Prefer the scoped calls above where they fit.

## See Also

### Related Documentation
- [Unified Memory](./unified-memory.md)
  `MLX` takes advantage of the shared memory between the CPU and GPU.
- [class Stream](./stream.md)
  A stream of evaluation attached to a particular device.
- [class Device](./device.md)
  Representation of a Device in MLX.
- [struct StreamOrDevice](./streamordevice.md)
  Parameter type for all MLX operations.
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
- [Running on iOS](./running-on-ios.md)
  Considerations for running on iOS and general memory tuning.
- [Wired Memory Management](./wired-memory.md)
  Coordinate a process-wide wired memory limit for GPU workloads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/using-streams)*