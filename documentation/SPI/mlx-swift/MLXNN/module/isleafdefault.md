---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/isleafdefault"
framework: "mlx-swift/MLXNN"
---

# isLeafDefault

**Framework**: mlx-swift/MLXNN  
**Kind**: property  
**Role**: Type Property

Default leaf filter – treat [`ModuleValue.parameters(_:)`](../modulevalue/parameters%28_%29.md) and [`ModuleValue.other(_:)`](../modulevalue/other%28_%29.md) as leaves.

## Declaration

```swift
static let isLeafDefault: @Sendable (Module, String, ModuleItem) -> Bool
```

#### Discussion

This will allow recursion into `.array`, `.dictionary` and [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md).

##### See Also

- [Module Filter and Map Functions](../module-filters.md)
- [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md)

## See Also

### isLeaf Functions
- [static let isLeafModule: (Module, String, ModuleItem) -> Bool](./isleafmodule.md)
  Leaf filter that will stop at [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md) and recurse into all other structure.
- [static let isLeafModuleNoChildren: (Module, String, ModuleItem) -> Bool](./isleafmodulenochildren.md)
  Leaf filter that will stop at [`ModuleValue.module(_:)`](../modulevalue/module%28_%29.md) if they have no child modules and recurse into all other structure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/isleafdefault)*