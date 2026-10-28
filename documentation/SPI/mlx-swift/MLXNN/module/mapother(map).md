---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapother(map:)"
framework: "mlx-swift/MLXNN"
---

# mapOther(map:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Type Method

Function that will turn a `(Any) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).

## Declaration

```swift
static func mapOther<Result>(map: @escaping (Any) -> Result? = { $0 }) -> (ModuleItem) -> Result?
```

## Discussion

For example:

```swift
// floatArguments is NestedDictionary<String, Float>
let floatArguments = module.mapParameters { other in
    other as? Float
}
```

### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`ModuleValue.other(_:)`](../modulevalue/other%28_%29.md)
- [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md)

## See Also

### Map Functions
- [static func mapModule<Result>(map: (Module) -> Result?) -> (ModuleItem) -> Result?](./mapmodule%28map%29.md)
  Function that will turn a `(Module) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).
- [static func mapParameters<Result>(map: (MLXArray) -> Result?) -> (ModuleItem) -> Result?](./mapparameters%28map%29.md)
  Function that will turn a `(MLXArray) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/mapother(map:))*