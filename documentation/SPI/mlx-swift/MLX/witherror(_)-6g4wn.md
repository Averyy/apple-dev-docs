---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherror(_:)-6g4wn"
framework: "mlx-swift/MLX"
---

# withError(_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Evaluate the block and convert MLX errors into Swift `throws` on block exit.

## Declaration

```swift
func withError<R>(_ body: () throws -> R) throws -> R
```

## Discussion

For example this will throw a Swift `Error`:

```swift
try withError {
    let a = MLXArray(0 ..< 10, [2, 5])
    let b = MLXArray(0 ..< 15, [3, 5])

    // this will trigger a broadcast error
    return a + b
}
```

Nested calls to `withError` produce scoped error collection.

### See Also

- [`withError(_:)`](./witherror%28_%29-2wfiu.md)
- [`withError(_:)`](./witherror%28_%29-4tvdu.md)

## Parameters

- `body`: The code where the handler is to be active


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherror(_:)-6g4wn)*