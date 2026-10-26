---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/updatable"
framework: "mlx-swift/MLX"
---

# Updatable

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

An object that can provide a list of the [`MLXArray`](./mlxarray.md) in its inner state.

## Declaration

```swift
protocol Updatable
```

#### Overview

Note that the array itself is not a reference to the inner state, but the [`MLXArray`](./mlxarray.md) instances can be [`MLXArray`](./mlxarray.md) to mutate the inner state.  The exact working is an implemention detail for MLX and should not be depended on by outside callers.

##### See Also

- [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md)

## Topics

### Instance Methods
- [func innerState() -> [MLXArray]](./updatable/innerstate%28%29.md)

## Relationships

### Conforming Types
- [Array](./swift/array.md)
- [MLXArray](./mlxarray.md)
- [MLXRandom.RandomState](./mlxrandom/randomstate.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/updatable)*