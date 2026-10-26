---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/modulevalue"
framework: "mlx-swift/MLXNN"
---

# ModuleValue

**Framework**: mlx-swift/MLXNN  
**Kind**: enum  
**Role**: Enumeration

A single value from [`Module`](./module.md).

## Declaration

```swift
enum ModuleValue
```

#### Overview

This is typically produced from [`items()`](./module/items%28%29.md) or indirectly via [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md).

##### See Also

- [`items()`](./module/items%28%29.md)
- [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md)
- [`ModuleItems`](./moduleitems.md)
- [`ModuleItem`](./moduleitem.md)

## Topics

### Enumeration Cases
- [ModuleValue.module(_:)](./modulevalue/module%28_%29.md)
  A module value.
- [ModuleValue.none](./modulevalue/none.md)
- [ModuleValue.other(_:)](./modulevalue/other%28_%29.md)
  A non-MLXArray and non-Module value.
- [ModuleValue.parameters(_:)](./modulevalue/parameters%28_%29.md)
  An `MLXArray` parameters value.
### Type Methods
- [static func fromMirror(Mirror.Child) -> (String, ModuleItem)?](./modulevalue/frommirror%28_%29.md)
  Return `(String, ModuleItem)` tuple or nil if the label cannot be determined.

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
- [typealias ModuleItems](./moduleitems.md)
  `NestedDictionary` structure of `ModuleValue` from [`items()`](./module/items%28%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/modulevalue)*