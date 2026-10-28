---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/devicetype"
framework: "mlx-swift/MLX"
---

# deviceType

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

The [`DeviceType`](../devicetype.md) for the device.

## Declaration

```swift
var deviceType: DeviceType { get }
```

## Discussion

Note: previously this returned an Optional [`DeviceType`](../devicetype.md).  Now it is not optional and it will be a `fatalError` if the DeviceType is unknown.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/devicetype)*