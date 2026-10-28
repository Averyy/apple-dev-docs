---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapmodule(map:)"
framework: "mlx-swift/MLXNN"
---

# mapModule(map:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Type Method

Function that will turn a `(Module) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).

## Declaration

```swift
static func mapModule<Result>(map: @escaping (Module) -> Result? = { $0 }) -> (ModuleItem) -> Result?
```

## Discussion

For example:

```swift
// typeNames is NestedDictionary<String, String>
let typeNames = module.mapParameters { module in
    String(describing: type(of: module))
}
```

### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md)
- [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md)

## See Also

### Map Functions
- [static func mapOther<Result>(map: (Any) -> Result?) -> (ModuleItem) -> Result?](./mapother%28map%29.md)
  Function that will turn a `(Any) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).
- [static func mapParameters<Result>(map: (MLXArray) -> Result?) -> (ModuleItem) -> Result?](./mapparameters%28map%29.md)
  Function that will turn a `(MLXArray) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapmodule(map:))*