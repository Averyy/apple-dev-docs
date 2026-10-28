---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/filtervalidparameters"
framework: "mlx-swift/MLXNN"
---

# filterValidParameters

**Framework**: mlx-swift/MLXNN  
**Kind**: property  
**Role**: Type Property

Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md) or [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md) allowing recursion into sub-Modules (layers).

## Declaration

```swift
static let filterValidParameters: @Sendable (Module, String, ModuleItem) -> Bool
```

### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`filterLocalParameters`](./filterlocalparameters.md)
- [`filterTrainableParameters`](./filtertrainableparameters.md)

## See Also

### Key/Value Filter Functions
- [static let filterAll: (Module, String, ModuleItem) -> Bool](./filterall.md)
  Filter that will accept all values.
- [static let filterLocalParameters: (Module, String, ModuleItem) -> Bool](./filterlocalparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md) without allowing recursion into sub-Modules (layers).
- [static let filterOther: (Module, String, ModuleItem) -> Bool](./filterother.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.other(_:)`](../modulevalue/other%28_%29.md).
- [static let filterTrainableParameters: (Module, String, ModuleItem) -> Bool](./filtertrainableparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md) or [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md) that are not in the `noGrad` set.
- [static let filterValidChild: (Module, String, ModuleItem) -> Bool](./filtervalidchild.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/filtervalidparameters)*