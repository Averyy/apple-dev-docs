---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayat"
framework: "mlx-swift/MLX"
---

# ArrayAt

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Intermediate type for [`at`](./mlxarray/at.md).

## Declaration

```swift
struct ArrayAt
```

#### Overview

This type isn’t typically used directly, rather it is the return value from the `at` property on MLXArray and provides the subscript.

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([0, 0])
a2 = a2.at[idx].add(1)
```

##### See Also

```
- ``MLXArray/at``
- ``ArrayAtIndices``
```

## Topics

### Subscripts
- [subscript(some Sequence<any MLXArrayIndex>, stream _: StreamOrDevice) -> ArrayAtIndices](./arrayat/subscript%28_,stream%29-3wf77.md)
  Provide indices for the `at` property:
- [subscript(any MLXArrayIndex..., stream _: StreamOrDevice) -> ArrayAtIndices](./arrayat/subscript%28_,stream%29-5co7x.md)
  Provide indices for the `at` property:


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayat)*