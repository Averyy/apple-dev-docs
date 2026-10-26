---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/freeze(recursive:keys:)"
framework: "mlx-swift/MLXNN"
---

# freeze(recursive:keys:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Non-throwing variant of [`freeze(recursive:keys:strict:)`](./freeze%28recursive,keys,strict%29.md) (`strict: false)`.

## Declaration

```swift
func freeze(recursive: Bool = true, keys: [String]? = nil)
```

## See Also

### Training
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./freeze%28recursive,keys,strict%29.md)
  Freeze the `Module`’s parameters or subset.
- [func train(Bool)](./train%28_%29.md)
  Recursively set the model’s training mode.
- [func unfreeze(recursive: Bool, keys: [String]?)](./unfreeze%28recursive,keys%29.md)
  Non-throwing variant of [`unfreeze(recursive:keys:strict:)`](./unfreeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func unfreeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./unfreeze%28recursive,keys,strict%29.md)
  Unfreeze the `Module`’s parameters or subset.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/freeze(recursive:keys:))*