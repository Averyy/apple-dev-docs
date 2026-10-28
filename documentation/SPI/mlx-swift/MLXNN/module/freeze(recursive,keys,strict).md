---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/freeze(recursive:keys:strict:)"
framework: "mlx-swift/MLXNN"
---

# freeze(recursive:keys:strict:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Freeze the `Module`’s parameters or subset.

## Declaration

```swift
func freeze(recursive: Bool = true, keys: [String]? = nil, strict: Bool = false) throws
```

## Mentions

- [Creating Modules](../custom-layers.md)

## Discussion

A frozen parameter does not compute gradients.  The function is idempotent – freezing a frozen model is a no-op.

For example to only train the attention parameters from a `Transformer`:

```swift
model: Transformer
model.freeze()
try model.visit { k, m in
    if k.hasSuffix("attention") {
        m.unfreeze()
    }
}
```

### See Also

- [`freeze(recursive:keys:)`](./freeze%28recursive,keys%29.md)
- [`unfreeze(recursive:keys:strict:)`](./unfreeze%28recursive,keys,strict%29.md)

## Parameters

- `recursive`: If `true` this will freeze the parameters of child `Module` recursively
- `keys`: Optional keys to freeze – if unspecified, will apply to all
- `strict`: If `true` validate that the passed keys exist

## See Also

### Training
- [func freeze(recursive: Bool, keys: [String]?)](./freeze%28recursive,keys%29.md)
  Non-throwing variant of [`freeze(recursive:keys:strict:)`](./freeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func train(Bool)](./train%28_%29.md)
  Recursively set the model’s training mode.
- [func unfreeze(recursive: Bool, keys: [String]?)](./unfreeze%28recursive,keys%29.md)
  Non-throwing variant of [`unfreeze(recursive:keys:strict:)`](./unfreeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func unfreeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./unfreeze%28recursive,keys,strict%29.md)
  Unfreeze the `Module`’s parameters or subset.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/freeze(recursive:keys:strict:))*