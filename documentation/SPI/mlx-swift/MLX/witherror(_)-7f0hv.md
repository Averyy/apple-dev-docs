---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherror(_:)-7f0hv"
framework: "mlx-swift/MLX"
---

# withError(_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Evaluate the block and convert MLX errors into Swift `throws` with explicit visibility of the error (async).

## Declaration

```swift
func withError<R>(_ body: (ErrorBox) async throws -> R) async throws -> R
```

#### Discussion

For example this will throw a Swift `Error`:

```swift
try await withError { error in
    let t = Task {
        let a = MLXArray(0 ..< 10, [2, 5])
        let b = MLXArray(0 ..< 15, [3, 5])

        // this will trigger a broadcast error
        let x = a + b

        // explicitly check for errors or return from the block
        try error.check()
        return x
    }
    try await t.value
}
```

Note: the `error` argument can be omitted to just check for errors on block exit. Nested calls to `withError` produce scoped error collection.

##### See Also

- [`withError(_:)`](./witherror%28_%29-2wfiu.md)
- [`withError(_:)`](./witherror%28_%29-4tvdu.md)

## Parameters

- `body`: The code where the handler is to be active


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherror(_:)-7f0hv)*