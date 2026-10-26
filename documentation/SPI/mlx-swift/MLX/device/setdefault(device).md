---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/setdefault(device:)"
framework: "mlx-swift/MLX"
---

# setDefault(device:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Set the default device globally.  Use the scoped version, [`withDefaultDevice(_:_:)`](./withdefaultdevice%28_,_%29-17vjl.md) – this is only usable before any mlx resources are created.

> **Deprecated**: use withDefaultDevice() -- this only works before any mlx resources are created

## Declaration

```swift
static func setDefault(device: Device?)
```

#### Discussion

Beware: using the static cpu and gpu values will render this unusable.  If required, call like this:

```swift
Device.setDefault(device: .init(.cpu))
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/setdefault(device:))*