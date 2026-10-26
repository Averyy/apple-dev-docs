---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/startcapture(url:)"
framework: "mlx-swift/MLX"
---

# startCapture(url:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Start capturing a metal trace into the given file.

## Declaration

```swift
static func startCapture(url: URL)
```

#### Discussion

> **Note**: There are several requirements for this to be used.

- `mlx` must be built with `MLX_METAL_DEBUG`

  - in Package.swift add `.define("MLX_METAL_DEBUG"),` to `Cmlx` `cxxSettings`
- when running set the `MTL_CAPTURE_ENABLED=1` environment variable
- make sure the file at the given path does not already exist

See [the documentation](https://ml-explore.github.io/mlx/build/html/dev/metal_debugger.html) for more information.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/gpu/startcapture(url:))*