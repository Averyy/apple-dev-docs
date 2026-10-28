---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/update(modules:verify:path:modulepath:)"
framework: "mlx-swift/MLXNN"
---

# update(modules:verify:path:modulePath:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Replace the child modules of this `Module` with the provided replacements.

## Declaration

```swift
@discardableResult
func update(modules: ModuleChildren, verify: Module.VerifyUpdate, path: [String] = [], modulePath: [String] = []) throws -> Self
```

## Mentions

- [Creating Modules](../custom-layers.md)

## Discussion

This will replace the parameters in the `Module` recursively with the given [`ModuleChildren`](../modulechildren.md) structure.  For example this is typically called via a helper function:

```swift
if let quantization = configuration.quantization {
    QuantizedLinear.quantize(model: model, groupSize: quantization.groupSize, bits: quantization.bits)
}
```

> **Note**: Note that the modules being replace must use a [`ModuleInfo`](../moduleinfo.md) property wrapper – this provides the mechanism to update the values.  Also note that the replacement models must be assignable to the ivar’s type.

For example:

```swift
public class FeedForward : Module {

    @ModuleInfo var w1: Linear
    @ModuleInfo var w2: Linear
    @ModuleInfo var w3: Linear
```

Would be able to be replaced with [`quantize(model:groupSize:bits:predicate:)`](../quantizedlinear/quantize%28model,groupsize,bits,predicate%29.md).

The `modules` need not provide all values in the model – any omitted values will be unchanged.

### See Also

- [Creating Modules](../custom-layers.md)
- [`update(modules:)`](./update%28modules%29.md)
- [`update(parameters:verify:path:modulePath:)`](./update%28parameters,verify,path,modulepath%29.md)
- [`children()`](./children%28%29.md)
- [`leafModules()`](./leafmodules%28%29.md)
- [`quantize(model:groupSize:bits:predicate:)`](../quantizedlinear/quantize%28model,groupsize,bits,predicate%29.md)

## Parameters

- `modules`: Replacement modules in the same format as [`children()`](./children%28%29.md) or [`leafModules()`](./leafmodules%28%29.md)
- `verify`: Options for verifying parameters
- `path`: The key path used for error reporting during recursive updates
- `modulePath`: The module type path used for error reporting during recursive updates

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
- [func visit(modules: (String, Module) throws -> Void) rethrows](./visit%28modules%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/update(modules:verify:path:modulepath:))*