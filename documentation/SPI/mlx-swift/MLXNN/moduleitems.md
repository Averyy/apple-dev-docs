---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/moduleitems"
framework: "mlx-swift/MLXNN"
---

# ModuleItems

**Framework**: mlx-swift/MLXNN  
**Kind**: typealias  
**Role**: Type Alias

`NestedDictionary` structure of `ModuleValue` from [`items()`](./module/items%28%29.md)

## Declaration

```swift
typealias ModuleItems = NestedDictionary<String, ModuleValue>
```

## See Also

### Base Classes and Interfaces
- [class Module](./module.md)
  Base class for building neural networks with MLX.
- [protocol UnaryLayer](./unarylayer.md)
  A `Layer` ([`Module`](./module.md) subclass) that can be evaluated as a *unary function*.
- [protocol Quantizable](./quantizable.md)
  Protocol for layers that can be quantized
- [class ModuleInfo](./moduleinfo.md)
  ModuleInfo can provde information about child modules and act as an update point for [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md).
- [class ParameterInfo](./parameterinfo.md)
  ParameterInfo allows you to specify alternate keys for parameter propreties.
- [typealias ModuleParameters](./moduleparameters.md)
  `NestedDictionary` structure of `MLXArray`
- [typealias ModuleChildren](./modulechildren.md)
  `NestedDictionary` structure of `Module`
- [typealias ModuleItem](./moduleitem.md)
  Single item from [`items()`](./module/items%28%29.md)
- [enum ModuleValue](./modulevalue.md)
  A single value from [`Module`](./module.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/moduleitems)*