---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherror(_:)-4tvdu"
framework: "mlx-swift/MLX"
---

# withError(_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Evaluate the block and convert MLX errors into Swift `throws` on block exit (async).

## Declaration

```swift
func withError<R>(_ body: () async throws -> R) async throws -> R
```

#### Discussion

For example this will throw a Swift `Error`:

```swift
try await withError {
    let t = Task {
        let a = MLXArray(0 ..< 10, [2, 5])
        let b = MLXArray(0 ..< 15, [3, 5])

        // this will trigger a broadcast error
        return a + b
    }
    await t.value
}
```

Nested calls to `withError` produce scoped error collection.

##### See Also

- [`withError(_:)`](./witherror%28_%29-6g4wn.md)
- [`withError(_:)`](./witherror%28_%29-7f0hv.md)

## Parameters

- `body`: The code where the handler is to be active


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/witherror(_:)-4tvdu)*