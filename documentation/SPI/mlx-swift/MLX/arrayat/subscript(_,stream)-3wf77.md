---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayat/subscript(_:stream:)-3wf77"
framework: "mlx-swift/MLX"
---

# subscript(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: subscript  
**Role**: Instance Subscript

Provide indices for the `at` property:

## Declaration

```swift
subscript(indices: some Sequence<any MLXArrayIndex>, stream stream: StreamOrDevice = .default) -> ArrayAtIndices { get }
```

## Overview

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([0, 0])
a2 = a2.at[idx].add(1)
```

This is specifically the `a2.at[idx]` part.

### See Also

```
- ``MLXArray/at``
- ``ArrayAtIndices``
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayat/subscript(_:stream:)-3wf77)*