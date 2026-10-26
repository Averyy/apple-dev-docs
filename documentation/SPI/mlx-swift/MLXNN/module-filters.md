---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module-filters"
framework: "mlx-swift/MLXNN"
---

# Module Filter and Map Functions

**Framework**: mlx-swift/MLXNN  
**Role**: API Collection

Pre-built filter and map functions in `Module`.

#### Overview

[`Module`](./module.md) provides a number of pre-build filter and map functions for use in:

- [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md)
- [`apply(filter:map:)`](./module/apply%28filter,map%29.md)
- [`mapParameters(map:isLeaf:)`](./module/mapparameters%28map,isleaf%29.md)

See those methods for more information.

#### Examples

The `filterMap()` method has several options for controlling the traversal of the modules, parameters and other values in the model.  Here is an example that limits the traversal to just local parameters and produces a `NestedDictionary` of the shapes:

```swift
// produces NestedDictionary<String, [Int]> for the parameters attached
// directly to this module
let localParameterShapes = module.filterMap(
    filter: Module.filterLocalParameters,
    map: Module.mapParameters { $0.shape })
```

Applying a map to the entire set of parameters (though some traversal control is possible through the optional `isLeaf`) is very easy:

```swift
let parameterShapes = module.mapParameters { $0.shape }
```

Finally, `apply()` does both a filter and an [`update(parameters:)`](./module/update%28parameters%29.md). This code would convert all floating point parameters to `.float16`.

```swift
layer.apply { array in
    array.dtype.isFloatingPoint ? array.asType(.float16) : array
}
```

## Topics

### Key/Value Filter Functions
- [static let filterAll: (Module, String, ModuleItem) -> Bool](./module/filterall.md)
  Filter that will accept all values.
- [static let filterLocalParameters: (Module, String, ModuleItem) -> Bool](./module/filterlocalparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) without allowing recursion into sub-Modules (layers).
- [static let filterOther: (Module, String, ModuleItem) -> Bool](./module/filterother.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.other(_:)`](./modulevalue/other%28_%29.md).
- [static let filterTrainableParameters: (Module, String, ModuleItem) -> Bool](./module/filtertrainableparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) or [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) that are not in the `noGrad` set.
- [static let filterValidChild: (Module, String, ModuleItem) -> Bool](./module/filtervalidchild.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md).
- [static let filterValidParameters: (Module, String, ModuleItem) -> Bool](./module/filtervalidparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) or [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) allowing recursion into sub-Modules (layers).
### isLeaf Functions
- [static let isLeafDefault: (Module, String, ModuleItem) -> Bool](./module/isleafdefault.md)
  Default leaf filter – treat [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) and [`ModuleValue.other(_:)`](./modulevalue/other%28_%29.md) as leaves.
- [static let isLeafModule: (Module, String, ModuleItem) -> Bool](./module/isleafmodule.md)
  Leaf filter that will stop at [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) and recurse into all other structure.
- [static let isLeafModuleNoChildren: (Module, String, ModuleItem) -> Bool](./module/isleafmodulenochildren.md)
  Leaf filter that will stop at [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) if they have no child modules and recurse into all other structure.
### Map Functions
- [static func mapModule<Result>(map: (Module) -> Result?) -> (ModuleItem) -> Result?](./module/mapmodule%28map%29.md)
  Function that will turn a `(Module) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md).
- [static func mapOther<Result>(map: (Any) -> Result?) -> (ModuleItem) -> Result?](./module/mapother%28map%29.md)
  Function that will turn a `(Any) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md).
- [static func mapParameters<Result>(map: (MLXArray) -> Result?) -> (ModuleItem) -> Result?](./module/mapparameters%28map%29.md)
  Function that will turn a `(MLXArray) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module-filters)*