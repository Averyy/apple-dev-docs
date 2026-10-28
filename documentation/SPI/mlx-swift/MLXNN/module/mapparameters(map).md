---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapparameters(map:)"
framework: "mlx-swift/MLXNN"
---

# mapParameters(map:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Type Method

Function that will turn a `(MLXArray) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).

## Declaration

```swift
static func mapParameters<Result>(map: @escaping (MLXArray) -> Result? = { $0 }) -> (ModuleItem) -> Result?
```

## Discussion

```swift
// map is (ModuleItem) -> [Int]?
let map = Module.mapParameters { array in
    array.shape
}

// shapes is NestedDictionary<String, [Int]>
let shapes = module.filterMap(filter: Module.filterValidParameters, map: map)
```

This is also trivially done with [`mapParameters(map:isLeaf:)`](./mapparameters%28map,isleaf%29.md), which uses this function internally:

```swift
let shapes = module.mapParameters { array in
    array.shape
}
```

### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md)
- [`mapParameters(map:isLeaf:)`](./mapparameters%28map,isleaf%29.md)
- [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md)

## See Also

### Map Functions
- [static func mapModule<Result>(map: (Module) -> Result?) -> (ModuleItem) -> Result?](./mapmodule%28map%29.md)
  Function that will turn a `(Module) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).
- [static func mapOther<Result>(map: (Any) -> Result?) -> (ModuleItem) -> Result?](./mapother%28map%29.md)
  Function that will turn a `(Any) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapparameters(map:))*