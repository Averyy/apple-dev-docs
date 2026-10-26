---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/apply(filter:map:)"
framework: "mlx-swift/MLXNN"
---

# apply(filter:map:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Apply a closure to the parameters in a `Module` recursively.

## Declaration

```swift
@discardableResult
func apply(filter: (Module, String, ModuleItem) -> Bool = Module.filterValidParameters, map: @escaping (MLXArray) -> MLXArray) -> Self
```

#### Discussion

For example to change all floating point parameters to `DType.float16`:

```swift
layer.apply { array in
    array.dtype.isFloatingPoint ? array.asType(.float16) : array
}
```

## Parameters

- `filter`: Filter for parameters to apply to
- `map`: Function to apply to the matched parameters

## See Also

### Parameters
- [func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./filtermap%28filter,map,isleaf%29.md)
  Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.
- [func mapParameters<Result>(map: (MLXArray) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./mapparameters%28map,isleaf%29.md)
  Apply a `map` to all parameters ([`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md)) in the module and its children.
- [func parameters() -> ModuleParameters](./parameters%28%29.md)
  Return a `NestedDictionary<String, MLXArray>` for all parameters in the model (all layers).
- [func trainableParameters() -> ModuleParameters](./trainableparameters%28%29.md)
  Return a `NestedDictionary<String, MLXArray>` for all trainable parameters in the model (all layers).
- [func update(parameters: ModuleParameters) -> Self](./update%28parameters%29.md)
  A non-throwing version of [`update(parameters:verify:path:modulePath:)`](./update%28parameters,verify,path,modulepath%29.md).
- [func update(parameters: ModuleParameters, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./update%28parameters,verify,path,modulepath%29.md)
  Replace the parameters of this `Module` with the provided parameters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/apply(filter:map:))*