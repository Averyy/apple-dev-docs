---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/updatemodule(key:_:)"
framework: "mlx-swift/MLXNN"
---

# updateModule(key:_:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Set a module to a new value.

## Declaration

```swift
func updateModule(key: String, _ value: Any) throws
```

## Discussion

The module property must be wrapped in a [`ModuleInfo`](../moduleinfo.md):

```swift
@ModuleInfo(key: "input_layernorm") var inputLayerNorm: RMSNorm
```

and the value must be a compatible type.

This method is called via [`update(modules:)`](./update%28modules%29.md) and is not typically called directly.  This is exposed as an overridable method for subclasses.

## Parameters

- `key`: Module key, see [`ModuleInfo`](../moduleinfo.md)
- `value`: The replacement module


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/updatemodule(key:_:))*