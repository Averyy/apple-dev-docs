---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherrorhandler(_:_:)-4ll5b"
framework: "mlx-swift/MLX"
---

# withErrorHandler(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Evaluate the block with a scoped MLX error handler.

## Declaration

```swift
func withErrorHandler<R>(_ handler: @escaping @Sendable (String) -> Void, _ body: () throws -> R) rethrows -> R
```

#### Discussion

For example this will print a message instead of exiting the process:

```swift
func printHandler(_ message: String) {
    print("Caught error: \(message)")
}

withErrorHandler(printHandler) {
    let a = MLXArray(0 ..< 10, [2, 5])
    let b = MLXArray(0 ..< 15, [3, 5])

    // this will trigger a broadcast error
    return a + b
}
```

Note: using the [`MLXArray`](./mlxarray.md) produced after an error will likely result in additional errors. See [`withError(_:)`](./witherror%28_%29-6g4wn.md) for examples that convert the errors into Swift `throws`.

##### See Also

- [`withError(_:)`](./witherror%28_%29-6g4wn.md)
- [`withError(_:)`](./witherror%28_%29-2wfiu.md)

## Parameters

- `handler`: The scoped handler
- `body`: The code where the handler is to be active


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherrorhandler(_:_:)-4ll5b)*