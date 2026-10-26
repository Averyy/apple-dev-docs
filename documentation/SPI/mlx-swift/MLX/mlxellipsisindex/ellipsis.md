---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxellipsisindex/ellipsis"
framework: "mlx-swift/MLX"
---

# ellipsis

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

Implementation of the `.ellipsis` MLXArray index.

## Declaration

```swift
static var ellipsis: MLXEllipsisIndex { get }
```

Available when `Self` is `MLXEllipsisIndex`.

#### Discussion

This is the equivalent of the `None` index in python:

```python
# python
array[0, ..., 1]
```

Written as this in swift:

```swift
// swift
array[0, .ellipsis, 1]
```

This is equivalent to inserting full range slices for all intermediate axes such that the `1` index fell on the last axis.

##### See Also

- [Indexing](../indexing.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxellipsisindex/ellipsis)*