---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/gpu"
framework: "mlx-swift/MLX"
---

# gpu

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Current GPU device.

## Declaration

```swift
static var gpu: Device { get }
```

#### Discussion

Note: previously this returned a `static` GPU device – it would always be index 0, even if there were multiple GPUs in the system.

##### See Also

- [`cpu`](./cpu.md)
- [`gpu`](../stream/gpu.md)
- [`withDefaultDevice(_:_:)`](./withdefaultdevice%28_,_%29-17vjl.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/gpu)*