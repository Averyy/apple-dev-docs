---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/visit(modules:)"
framework: "mlx-swift/MLXNN"
---

# visit(modules:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func visit(modules visitor: (String, Module) throws -> Void) rethrows
```

## See Also

### Layers (sub-modules)
- [func children() -> ModuleChildren](./children%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all direct children of the module.
- [func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./filtermap%28filter,map,isleaf%29.md)
  Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.
- [func leafModules() -> ModuleChildren](./leafmodules%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all leaf modules module.
- [func modules() -> [Module]](./modules%28%29.md)
  Return a flat array of all the `Module` in the instance (including self).
- [func namedModules() -> [(String, Module)]](./namedmodules%28%29.md)
  Return a flat array of all the `Module` in the instance (including self) with their keys.
- [func update(modules: ModuleChildren) -> Self](./update%28modules%29.md)
  A non-throwing version of [`update(modules:verify:path:modulePath:)`](./update%28modules,verify,path,modulepath%29.md).
- [func update(modules: ModuleChildren, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./update%28modules,verify,path,modulepath%29.md)
  Replace the child modules of this `Module` with the provided replacements.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/visit(modules:))*