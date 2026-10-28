---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/tensordot(_:_:axes:stream:)-5ne6c"
framework: "mlx-swift/MLX"
---

# tensordot(_:_:axes:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Compute tensor dot product.

## Declaration

```swift
func tensordot(_ a: MLXArray, _ b: MLXArray, axes: (some Collection<Int>, some Collection<Int>), stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

Tensor dot product

### See Also

- [Arithmetic](./arithmetic.md)
- [`tensordot(_:_:axes:stream:)`](./tensordot%28_,_,axes,stream%29-5ne6c.md)

## Parameters

- `a`: Input array
- `b`: Input array
- `axes`: Multiple ranges for the `a` and `b` dimensions
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/tensordot(_:_:axes:stream:)-5ne6c)*