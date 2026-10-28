---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/using(device:fn:)"
framework: "mlx-swift/MLX"
---

# using(device:fn:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Execute a block of code using a specific device.

> **Deprecated**: please use Device.withDefaultDevice()

## Declaration

```swift
func using<R>(device: Device, fn: () throws -> R) rethrows -> R
```

## Discussion

Example:

```swift
using(device: .gpu) {
   // code here will run on the GPU
}
```

## Parameters

- `device`: Device to be used
- `fn`: Function to be executed


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/using(device:fn:))*