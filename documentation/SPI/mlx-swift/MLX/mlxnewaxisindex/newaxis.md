---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxnewaxisindex/newaxis"
framework: "mlx-swift/MLX"
---

# newAxis

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Implementation of the `.newAxis`MLXArray index.

## Declaration

```swift
static var newAxis: MLXNewAxisIndex { get }
```

Available when `Self` is `MLXNewAxisIndex`.

#### Discussion

This is the equivalent of the `None` index in python:

```python
# python
array[0, None]
```

Written as this in swift:

```swift
// swift
array[0, .newAxis]
```

##### See Also

- [Indexing](../indexing.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxnewaxisindex/newaxis)*