---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapparameters(map:isleaf:)"
framework: "mlx-swift/MLXNN"
---

# mapParameters(map:isLeaf:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Apply a `map` to all parameters ([`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md)) in the module and its children.

## Declaration

```swift
func mapParameters<Result>(map: @escaping (MLXArray) -> Result? = { $0 }, isLeaf: (Module, String, ModuleItem) -> Bool = Module.isLeafDefault) -> NestedDictionary<String, Result>
```

## Mentions

- [Creating Modules](../custom-layers.md)

## Return Value

`NestedDictionary` of mapped results

## Discussion

For example:

```swift
// shapes is NestedDictionary<String, [Int]>
let shapes = module.mapParameters { array in
    array.shape
}
```

This is equivalent to:

```swift
filterMap(
    filter: Self.filterValidParameters,
    map: Self.mapParameters(map: map),
    isLeaf: isLeaf)
```

### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`mapParameters(map:)`](./mapparameters%28map%29.md)

## Parameters

- `map`: Closure that transforms `MLXArray` into `Result` type or nil
- `isLeaf`: Optional leaf function

## See Also

### Parameters
- [func apply(filter: (Module, String, ModuleItem) -> Bool, map: (MLXArray) -> MLXArray) -> Self](./apply%28filter,map%29.md)
  Apply a closure to the parameters in a `Module` recursively.
- [func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./filtermap%28filter,map,isleaf%29.md)
  Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.
- [func parameters() -> ModuleParameters](./parameters%28%29.md)
  Return a `NestedDictionary<String, MLXArray>` for all parameters in the model (all layers).
- [func trainableParameters() -> ModuleParameters](./trainableparameters%28%29.md)
  Return a `NestedDictionary<String, MLXArray>` for all trainable parameters in the model (all layers).
- [func update(parameters: ModuleParameters) -> Self](./update%28parameters%29.md)
  A non-throwing version of [`update(parameters:verify:path:modulePath:)`](./update%28parameters,verify,path,modulepath%29.md).
- [func update(parameters: ModuleParameters, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./update%28parameters,verify,path,modulepath%29.md)
  Replace the parameters of this `Module` with the provided parameters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapparameters(map:isleaf:))*