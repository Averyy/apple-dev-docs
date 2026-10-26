---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/train(_:)"
framework: "mlx-swift/MLXNN"
---

# train(_:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Recursively set the model’s training mode.

## Declaration

```swift
func train(_ mode: Bool = true)
```

#### Discussion

Training mode only applies to certain layers. For example [`Dropout`](../dropout.md) applies a random mask in training mode, but is the identity in evaluation mode.

##### See Also

- [`training`](./training.md)
- [`didSetTrain(_:)`](./didsettrain%28_%29.md)

## See Also

### Training
- [func freeze(recursive: Bool, keys: [String]?)](./freeze%28recursive,keys%29.md)
  Non-throwing variant of [`freeze(recursive:keys:strict:)`](./freeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./freeze%28recursive,keys,strict%29.md)
  Freeze the `Module`’s parameters or subset.
- [func unfreeze(recursive: Bool, keys: [String]?)](./unfreeze%28recursive,keys%29.md)
  Non-throwing variant of [`unfreeze(recursive:keys:strict:)`](./unfreeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func unfreeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./unfreeze%28recursive,keys,strict%29.md)
  Unfreeze the `Module`’s parameters or subset.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/train(_:))*