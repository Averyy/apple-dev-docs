---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/update(parameters:verify:path:modulepath:)"
framework: "mlx-swift/MLXNN"
---

# update(parameters:verify:path:modulePath:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Replace the parameters of this `Module` with the provided parameters.

## Declaration

```swift
@discardableResult
func update(parameters: ModuleParameters, verify: Module.VerifyUpdate, path: [String] = [], modulePath: [String] = []) throws -> Self
```

## Mentions

- [Creating Modules](../custom-layers.md)

## Discussion

This will replace the parameters in the `Module` recursively with the given [`ModuleParameters`](../moduleparameters.md) structure.  For example:

```swift
// double all the parameters in the model
model.update(parameters: module.mapParameters(map: { $0 * 2 })

// equivalent to
model.apply { $0 * 2 }
```

The `parameters` need not provide all values in the model – any omitted values will be unchanged.

The [`apply(filter:map:)`](./apply%28filter,map%29.md) can be used for similar purposes to apply changes in-place.

> **Note**: If this module is used inside a compiled closure (`compile()`) that does not list the module in `inputs:`, calling `update(parameters:)` after the first compiled call will not be observed by the compiled function – `inputs:` is what makes `compile` re-read current parameter values on every call. `outputs:` is only needed in addition when the compiled closure itself mutates this module’s parameters and the mutation should be written back.

If a parameter is missing from the update and validation indicates `.allModelKeysSet` this will call [`updateMissing(parameter:verify:path:modulePath:)`](./updatemissing%28parameter,verify,path,modulepath%29.md) which will throw an error.  Subclasses can override this if needed.

### See Also

- [Creating Modules](../custom-layers.md)
- [`update(parameters:)`](./update%28parameters%29.md)
- [`apply(filter:map:)`](./apply%28filter,map%29.md)
- [`parameters()`](./parameters%28%29.md)
- [`mapParameters(map:isLeaf:)`](./mapparameters%28map,isleaf%29.md)
- [`update(modules:verify:path:modulePath:)`](./update%28modules,verify,path,modulepath%29.md)

## Parameters

- `parameters`: Replacement parameters in the same format that [`parameters()`](./parameters%28%29.md) or [`mapParameters(map:isLeaf:)`](./mapparameters%28map,isleaf%29.md) provides
- `verify`: Options for verifying parameters
- `path`: The key path used for error reporting during recursive updates
- `modulePath`: The module type path used for error reporting during recursive updates

## See Also

### Parameters
- [func apply(filter: (Module, String, ModuleItem) -> Bool, map: (MLXArray) -> MLXArray) -> Self](./apply%28filter,map%29.md)
  Apply a closure to the parameters in a `Module` recursively.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/update(parameters:verify:path:modulepath:))*