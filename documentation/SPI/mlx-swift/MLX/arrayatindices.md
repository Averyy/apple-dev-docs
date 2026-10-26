---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices"
framework: "mlx-swift/MLX"
---

# ArrayAtIndices

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Intermediate type for [`at`](./mlxarray/at.md).

## Declaration

```swift
struct ArrayAtIndices
```

#### Overview

This type allows update operations when using `array.at[indices]`, e.g.:

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([0, 0])
a2 = a2.at[idx].add(1)
```

##### See Also

```
- ``MLXArray/at``
- ``ArrayAt``
```

## Topics

### Instance Methods
- [func add(some ScalarOrArray) -> MLXArray](./arrayatindices/add%28_%29.md)
  Add values via `at[]` operator.
- [func divide(some ScalarOrArray) -> MLXArray](./arrayatindices/divide%28_%29.md)
  Divide values via `at[]` operator.
- [func maximum(some ScalarOrArray) -> MLXArray](./arrayatindices/maximum%28_%29.md)
  Update to maximum values via `at[]` operator.
- [func minimum(some ScalarOrArray) -> MLXArray](./arrayatindices/minimum%28_%29.md)
  Update to minimum values via `at[]` operator.
- [func multiply(some ScalarOrArray) -> MLXArray](./arrayatindices/multiply%28_%29.md)
  Multiply values via `at[]` operator.
- [func subtract(some ScalarOrArray) -> MLXArray](./arrayatindices/subtract%28_%29.md)
  Subtract values via `at[]` operator.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices)*