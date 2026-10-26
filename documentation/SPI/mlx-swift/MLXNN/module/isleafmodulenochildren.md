---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/isleafmodulenochildren"
framework: "mlx-swift/MLXNN"
---

# isLeafModuleNoChildren

**Framework**: mlx-swift/MLXNN  
**Kind**: property  
**Role**: Type Property

Leaf filter that will stop at [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md) if they have no child modules and recurse into all other structure.

## Declaration

```swift
static let isLeafModuleNoChildren: @Sendable (Module, String, ModuleItem) -> Bool
```

##### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md)

## See Also

### isLeaf Functions
- [static let isLeafDefault: (Module, String, ModuleItem) -> Bool](./isleafdefault.md)
  Default leaf filter – treat [`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md) and [`ModuleValue.other(_:)`](../modulevalue/other%28_%29.md) as leaves.
- [static let isLeafModule: (Module, String, ModuleItem) -> Bool](./isleafmodule.md)
  Leaf filter that will stop at [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md) and recurse into all other structure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/isleafmodulenochildren)*