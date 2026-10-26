---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/streamordevice/device(_:)"
framework: "mlx-swift/MLX"
---

# device(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Evaluate on the given [`Device`](../device.md).

> **Deprecated**: prefer stream(Stream)

## Declaration

```swift
static func device(_ device: Device) -> StreamOrDevice
```

#### Discussion

Prefer [`cpu`](./cpu.md) and [`gpu`](./gpu.md) instead as they will use the current Device for the Task.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/streamordevice/device(_:))*