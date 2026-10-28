---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/parameterinfo"
framework: "mlx-swift/MLXNN"
---

# ParameterInfo

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

ParameterInfo allows you to specify alternate keys for parameter propreties.

## Declaration

```swift
@propertyWrapper
class ParameterInfo<T>
```

## Mentions

- [Creating Modules](./custom-layers.md)

## Overview

For example:

```swift
class MyLayer : Module {

    let weights: MLXArray
    @ParameterInfo(key: "bias") var b: MLXArray
}
```

will have keys `weights` and `bias`.

### See Also

- [Creating Modules](./custom-layers.md)
- [`ModuleInfo`](./moduleinfo.md)

## Topics

### Initializers
- [init(key: String?)](./parameterinfo/init%28key%29.md)
- [init(wrappedValue: T, key: String?)](./parameterinfo/init%28wrappedvalue,key%29.md)
### Instance Properties
- [var wrappedValue: T](./parameterinfo/wrappedvalue.md)

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
- [typealias ModuleParameters](./moduleparameters.md)
  `NestedDictionary` structure of `MLXArray`
- [typealias ModuleChildren](./modulechildren.md)
  `NestedDictionary` structure of `Module`
- [typealias ModuleItem](./moduleitem.md)
  Single item from [`items()`](./module/items%28%29.md)
- [typealias ModuleItems](./moduleitems.md)
  `NestedDictionary` structure of `ModuleValue` from [`items()`](./module/items%28%29.md)
- [enum ModuleValue](./modulevalue.md)
  A single value from [`Module`](./module.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/parameterinfo)*