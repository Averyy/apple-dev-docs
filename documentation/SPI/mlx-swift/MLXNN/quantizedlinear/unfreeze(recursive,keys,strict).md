---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/unfreeze(recursive:keys:strict:)"
framework: "mlx-swift/MLXNN"
---

# unfreeze(recursive:keys:strict:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Unfreeze the `Module`’s parameters or subset.

## Declaration

```swift
override func unfreeze(recursive: Bool = true, keys: [String]? = nil, strict: Bool = false) throws
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

- [`freeze(recursive:keys:)`](../module/freeze%28recursive,keys%29.md)
- [`unfreeze(recursive:keys:strict:)`](../module/unfreeze%28recursive,keys,strict%29.md)

## Parameters

- `recursive`: If `true` this will unfreeze the parameters of child `Module` recursively
- `keys`: Optional keys to unfreeze – if unspecified, will apply to all
- `strict`: If `true` validate that the passed keys exist


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear/unfreeze(recursive:keys:strict:))*