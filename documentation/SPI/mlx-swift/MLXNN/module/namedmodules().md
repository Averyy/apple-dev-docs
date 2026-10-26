---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/namedmodules()"
framework: "mlx-swift/MLXNN"
---

# namedModules()

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Return a flat array of all the `Module` in the instance (including self) with their keys.

## Declaration

```swift
func namedModules() -> [(String, Module)]
```

##### See Also

- [`modules()`](./modules%28%29.md)
- [`children()`](./children%28%29.md)
- [`leafModules()`](./leafmodules%28%29.md)

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
- [func update(modules: ModuleChildren) -> Self](./update%28modules%29.md)
  A non-throwing version of [`update(modules:verify:path:modulePath:)`](./update%28modules,verify,path,modulepath%29.md).
- [func update(modules: ModuleChildren, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./update%28modules,verify,path,modulepath%29.md)
  Replace the child modules of this `Module` with the provided replacements.
- [func visit(modules: (String, Module) throws -> Void) rethrows](./visit%28modules%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/namedmodules())*