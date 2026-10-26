---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/unfreeze(recursive:keys:strict:)"
framework: "mlx-swift/MLXNN"
---

# unfreeze(recursive:keys:strict:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Unfreeze the `Module`’s parameters or subset.

## Declaration

```swift
func unfreeze(recursive: Bool = true, keys: [String]? = nil, strict: Bool = false) throws
```

#### Discussion

A frozen parameter does not compute gradients.  The function is idempotent – unfreezing a frozen model is a no-op.

For instance to only train the biases of a `Transformer` one can do:

```swift
model: Transformer
model.freeze()
try model.unfreeze(keys: ["bias"])
```

##### See Also

- [`freeze(recursive:keys:)`](./freeze%28recursive,keys%29.md)
- [`unfreeze(recursive:keys:strict:)`](./unfreeze%28recursive,keys,strict%29.md)

## Parameters

- `recursive`: If `true` this will unfreeze the parameters of child `Module` recursively
- `keys`: Optional keys to unfreeze – if unspecified, will apply to all
- `strict`: If `true` validate that the passed keys exist

## See Also

### Training
- [func freeze(recursive: Bool, keys: [String]?)](./freeze%28recursive,keys%29.md)
  Non-throwing variant of [`freeze(recursive:keys:strict:)`](./freeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./freeze%28recursive,keys,strict%29.md)
  Freeze the `Module`’s parameters or subset.
- [func train(Bool)](./train%28_%29.md)
  Recursively set the model’s training mode.
- [func unfreeze(recursive: Bool, keys: [String]?)](./unfreeze%28recursive,keys%29.md)
  Non-throwing variant of [`unfreeze(recursive:keys:strict:)`](./unfreeze%28recursive,keys,strict%29.md) (`strict: false)`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/unfreeze(recursive:keys:strict:))*