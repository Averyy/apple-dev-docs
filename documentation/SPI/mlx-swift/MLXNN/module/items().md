---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/items()"
framework: "mlx-swift/MLXNN"
---

# items()

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Return a `NestedDictionary` structure of [`ModuleItem`](../moduleitem.md) representing the ivars of the `Module` instance.

## Declaration

```swift
func items() -> ModuleItems
```

#### Discussion

This is typically not used directly – it is part of the implementation of [`filterMap(filter:map:isLeaf:)`](./filtermap%28filter,map,isleaf%29.md) and [`update(parameters:)`](./update%28parameters%29.md) for example.

Subclasses could potentially override this to provide custom introspection.

## See Also

### Traversal
- [func children() -> ModuleChildren](./children%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all direct children of the module.
- [func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./filtermap%28filter,map,isleaf%29.md)
  Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.
- [func leafModules() -> ModuleChildren](./leafmodules%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all leaf modules module.
- [func visit(modules: (String, Module) throws -> Void) rethrows](./visit%28modules%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/items())*