---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/filtermap(filter:map:isleaf:)"
framework: "mlx-swift/MLXNN"
---

# filterMap(filter:map:isLeaf:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.

## Declaration

```swift
func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result? = { $0 }, isLeaf: (Module, String, ModuleItem) -> Bool = Module.isLeafDefault) -> NestedDictionary<String, Result>
```

#### Return Value

`NestedDictionary` matching the structure with mapped values.

#### Discussion

Traverses the [`ModuleItems`](../moduleitems.md) produced by [`items()`](./items%28%29.md) and filters and maps their contents.  For each item in the `ModuleItems` this will call the `filter` to determine if it should be included.  There are a number of predefined filters available, see [Module Filter and Map Functions](../module-filters.md).  [`filterAll`](./filterall.md) will accept all values while [`filterValidParameters`](./filtervalidparameters.md) will only examine structure and parameters.

The `map` function transforms the visited values.  By default it is identity and will just return the [`ModuleItem`](../moduleitem.md) directly.  There are a number of helper functions like [`mapParameters(map:)`](./mapparameters%28map%29.md) and [`mapModule(map:)`](./mapmodule%28map%29.md) that can help deal with types like `MLXArray` or [`Module`](../module.md).  For example:

```swift
// produces NestedDictionary<String, [Int]> for the parameters attached
// directly to this module
let localParameterShapes = module.filterMap(
    filter: Module.filterLocalParameters,
    map: Module.mapParameters { $0.shape })
```

The `isLeaf` function is called to determine if the value should be transformed via the `map` or if the structure should be traversed.  For example this will collect the leaf modules:

```swift
// produces NestedDictionary<String, MLXArray> for all leaf modules
let leafParameters = module.filterMap(
    filter: Module.filterValidParameters,
    map: Module.mapParameters { $0 },
    isLeaf: Module.isLeafModuleNoChildren)
```

##### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`parameters()`](./parameters%28%29.md)
- [`mapParameters(map:isLeaf:)`](./mapparameters%28map,isleaf%29.md)
- [`modules()`](./modules%28%29.md)
- [`items()`](./items%28%29.md)

## Parameters

- `filter`: Filter function that determines if the (Module, Key, Item) tuple should be examined
- `map`: Transformation of the values.  By default this is identity but the caller can transform to other types, etc.  See [`mapParameters(map:)`](./mapparameters%28map%29.md) and others for helper functions that can assist with common types.
- `isLeaf`: Closure that determines if a value is a leaf or not.

## See Also

### Parameters
- [func apply(filter: (Module, String, ModuleItem) -> Bool, map: (MLXArray) -> MLXArray) -> Self](./apply%28filter,map%29.md)
  Apply a closure to the parameters in a `Module` recursively.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/filtermap(filter:map:isleaf:))*