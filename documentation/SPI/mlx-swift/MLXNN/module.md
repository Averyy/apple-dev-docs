---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module"
framework: "mlx-swift/MLXNN"
---

# Module

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Base class for building neural networks with MLX.

## Declaration

```swift
class Module
```

## Mentions

- [Creating Modules](./custom-layers.md)

#### Overview

The workhorse of any neural network library is the [`Module`](./module.md) class. In MLX the [`Module`](./module.md) class is a container of `MLXArray` or [`Module`](./module.md) instances. Its main function is to provide a way to recursively access and update its parameters and those of its submodules.

All the layers provided in [Layers](./layers.md) subclass this class and your models should do the same.  See [Creating Modules](./custom-layers.md).

##### Parameters

A `Module` can contain other `Module` instances or `MLXArray` instances in structures of `Array` and `Dictionary`. The `Module` then allows recursively extracting all the `MLXArray` instances using [`parameters()`](./module/parameters%28%29.md)

In addition, the `Module` has the concept of trainable and non trainable parameters (called “frozen”). When using `valueAndGrad()` or `grad()` the gradients are returned only with respect to the trainable parameters. All arrays in a module are trainable unless they are added in the “frozen” set by calling [`freeze(recursive:keys:strict:)`](./module/freeze%28recursive,keys,strict%29.md).

[`valueAndGrad(model:_:)`](./valueandgrad%28model,_%29-12a2c.md) the gradients returned will be with respect to these trainable parameters.

##### Example

Here is an example multi-layer perception (MLP):

```swift
import MLX
import MLXNN

class MyMLP : Module, UnaryLayer {
    let inProjection: Linear
    let outProjection: Linear

    init(inputDimensions: Int, outputDimensions: Int, hiddenDimensions: Int = 16) {
        self.inProjection = Linear(inputDimensions, hiddenDimensions)
        sel.outProjection = Linear(hiddenDimensions, outputDimensions)
    }

    func callAsFunction(_ x: MLXArray) -> MLXArray {
        var x = inProjection(x)
        x = maximum(x, 0)
        return outProjection(x)
    }
}

let model = MyMLP(inputDimensions: 2, outputDimensions: 1)

// All the model parameters are created but since MLX is lazy by
// default, they are not evaluated yet. Calling `eval` actually
// allocates memory and initializes the parameters.
eval(model)

// and projecting a value through the model:
let input: MLXArray ...
let result = model(input)
```

> **Note**: Please read [Creating Modules](./custom-layers.md) for more information about implementing custom layers including how to override the module and parameter keys and allowing dynamic updates of the module structure to occur via [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md).

##### Training

See [Training a Model](./training.md)

##### Mutation

All mutation of parameters and modules must go through [`update(parameters:)`](./module/update%28parameters%29.md) and [`update(modules:)`](./module/update%28modules%29.md).  This is important because `Module` uses reflection (`Mirror`) to find parameters and modules but caches the values.  These two methods make sure the cache is kept up-to-date.

##### See Also

- [Creating Modules](./custom-layers.md)

## Topics

### Parameters
- [func apply(filter: (Module, String, ModuleItem) -> Bool, map: (MLXArray) -> MLXArray) -> Self](./module/apply%28filter,map%29.md)
  Apply a closure to the parameters in a `Module` recursively.
- [func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./module/filtermap%28filter,map,isleaf%29.md)
  Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.
- [func mapParameters<Result>(map: (MLXArray) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./module/mapparameters%28map,isleaf%29.md)
  Apply a `map` to all parameters ([`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md)) in the module and its children.
- [func parameters() -> ModuleParameters](./module/parameters%28%29.md)
  Return a `NestedDictionary<String, MLXArray>` for all parameters in the model (all layers).
- [func trainableParameters() -> ModuleParameters](./module/trainableparameters%28%29.md)
  Return a `NestedDictionary<String, MLXArray>` for all trainable parameters in the model (all layers).
- [func update(parameters: ModuleParameters) -> Self](./module/update%28parameters%29.md)
  A non-throwing version of [`update(parameters:verify:path:modulePath:)`](./module/update%28parameters,verify,path,modulepath%29.md).
- [func update(parameters: ModuleParameters, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./module/update%28parameters,verify,path,modulepath%29.md)
  Replace the parameters of this `Module` with the provided parameters.
### Layers (sub-modules)
- [func children() -> ModuleChildren](./module/children%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all direct children of the module.
- [func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./module/filtermap%28filter,map,isleaf%29.md)
  Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.
- [func leafModules() -> ModuleChildren](./module/leafmodules%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all leaf modules module.
- [func modules() -> [Module]](./module/modules%28%29.md)
  Return a flat array of all the `Module` in the instance (including self).
- [func namedModules() -> [(String, Module)]](./module/namedmodules%28%29.md)
  Return a flat array of all the `Module` in the instance (including self) with their keys.
- [func update(modules: ModuleChildren) -> Self](./module/update%28modules%29.md)
  A non-throwing version of [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md).
- [func update(modules: ModuleChildren, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./module/update%28modules,verify,path,modulepath%29.md)
  Replace the child modules of this `Module` with the provided replacements.
- [func visit(modules: (String, Module) throws -> Void) rethrows](./module/visit%28modules%29.md)
### Traversal
- [func children() -> ModuleChildren](./module/children%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all direct children of the module.
- [func filterMap<Result>(filter: (Module, String, ModuleItem) -> Bool, map: (ModuleItem) -> Result?, isLeaf: (Module, String, ModuleItem) -> Bool) -> NestedDictionary<String, Result>](./module/filtermap%28filter,map,isleaf%29.md)
  Recursively filter and map the contents of the module and its children and produce a `NestedDictionary` with the results.
- [func leafModules() -> ModuleChildren](./module/leafmodules%28%29.md)
  Produces a `NestedDictionary<String, Module>` for all leaf modules module.
- [func items() -> ModuleItems](./module/items%28%29.md)
  Return a `NestedDictionary` structure of [`ModuleItem`](./moduleitem.md) representing the ivars of the `Module` instance.
- [func visit(modules: (String, Module) throws -> Void) rethrows](./module/visit%28modules%29.md)
### Module and Parameter Filtering
- [Module Filter and Map Functions](./module-filters.md)
  Pre-built filter and map functions in `Module`.
### Training
- [func freeze(recursive: Bool, keys: [String]?)](./module/freeze%28recursive,keys%29.md)
  Non-throwing variant of [`freeze(recursive:keys:strict:)`](./module/freeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./module/freeze%28recursive,keys,strict%29.md)
  Freeze the `Module`’s parameters or subset.
- [func train(Bool)](./module/train%28_%29.md)
  Recursively set the model’s training mode.
- [func unfreeze(recursive: Bool, keys: [String]?)](./module/unfreeze%28recursive,keys%29.md)
  Non-throwing variant of [`unfreeze(recursive:keys:strict:)`](./module/unfreeze%28recursive,keys,strict%29.md) (`strict: false)`.
- [func unfreeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./module/unfreeze%28recursive,keys,strict%29.md)
  Unfreeze the `Module`’s parameters or subset.
### Key/Value Filter Functions
- [static let filterAll: (Module, String, ModuleItem) -> Bool](./module/filterall.md)
  Filter that will accept all values.
- [static let filterLocalParameters: (Module, String, ModuleItem) -> Bool](./module/filterlocalparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) without allowing recursion into sub-Modules (layers).
- [static let filterOther: (Module, String, ModuleItem) -> Bool](./module/filterother.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.other(_:)`](./modulevalue/other%28_%29.md).
- [static let filterTrainableParameters: (Module, String, ModuleItem) -> Bool](./module/filtertrainableparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) or [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) that are not in the `noGrad` set.
- [static let filterValidChild: (Module, String, ModuleItem) -> Bool](./module/filtervalidchild.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md).
- [static let filterValidParameters: (Module, String, ModuleItem) -> Bool](./module/filtervalidparameters.md)
  Filter that will accept all structure (`.array` and `.dictionary`) and [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) or [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) allowing recursion into sub-Modules (layers).
### isLeaf Functions
- [static let isLeafDefault: (Module, String, ModuleItem) -> Bool](./module/isleafdefault.md)
  Default leaf filter – treat [`ModuleValue.parameters(_:)`](./modulevalue/parameters%28_%29.md) and [`ModuleValue.other(_:)`](./modulevalue/other%28_%29.md) as leaves.
- [static let isLeafModule: (Module, String, ModuleItem) -> Bool](./module/isleafmodule.md)
  Leaf filter that will stop at [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) and recurse into all other structure.
- [static let isLeafModuleNoChildren: (Module, String, ModuleItem) -> Bool](./module/isleafmodulenochildren.md)
  Leaf filter that will stop at [`ModuleValue.module(_:)`](./modulevalue/module%28_%29.md) if they have no child modules and recurse into all other structure.
### Map Functions
- [static func mapModule<Result>(map: (Module) -> Result?) -> (ModuleItem) -> Result?](./module/mapmodule%28map%29.md)
  Function that will turn a `(Module) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md).
- [static func mapOther<Result>(map: (Any) -> Result?) -> (ModuleItem) -> Result?](./module/mapother%28map%29.md)
  Function that will turn a `(Any) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md).
- [static func mapParameters<Result>(map: (MLXArray) -> Result?) -> (ModuleItem) -> Result?](./module/mapparameters%28map%29.md)
  Function that will turn a `(MLXArray) -> Result?` into a function suitable for use in [`filterMap(filter:map:isLeaf:)`](./module/filtermap%28filter,map,isleaf%29.md).
### Structures
- [Module.VerifyUpdate](./module/verifyupdate.md)
  Options for verifying [`update(parameters:verify:path:modulePath:)`](./module/update%28parameters,verify,path,modulepath%29.md) and [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md).
### Initializers
- [init()](./module/init%28%29.md)
  Initializes the module.
### Instance Properties
- [var training: Bool](./module/training.md)
  Flag to indicate whether the module is being trained.  Manipulated via [`train(_:)`](./module/train%28_%29.md).
### Instance Methods
- [func describeExtra(Int) -> String](./module/describeextra%28_%29.md)
  Describe extra parameters.
- [func didSetNoGrad(Set<String>)](./module/didsetnograd%28_%29.md)
  Called when [`noGrad()`](./module/nograd%28%29.md) is updated.
- [func didSetTrain(Bool)](./module/didsettrain%28_%29.md)
  Called when [`train(_:)`](./module/train%28_%29.md) is updated.
- [func noGrad() -> Set<String>](./module/nograd%28%29.md)
  Set of property names that are frozen.  Manipulated via [`freeze(recursive:keys:strict:)`](./module/freeze%28recursive,keys,strict%29.md) and [`unfreeze(recursive:keys:strict:)`](./module/unfreeze%28recursive,keys,strict%29.md).
- [func updateMissing(parameter: String, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws](./module/updatemissing%28parameter,verify,path,modulepath%29.md)
  Called from [`update(parameters:verify:path:modulePath:)`](./module/update%28parameters,verify,path,modulepath%29.md) if a required parameter is missing.
- [func updateModule(key: String, Any) throws](./module/updatemodule%28key,_%29.md)
  Set a module to a new value.
### Type Methods
- [static func parameterIsValid(String) -> Bool](./module/parameterisvalid%28_%29.md)
  Return `true` if the given parameter name is valid – should be considered for validation, enumeration, etc.
### Default Implementations
- [CustomStringConvertible Implementations](./module/customstringconvertible-implementations.md)
- [IndentedDescription Implementations](./module/indenteddescription-implementations.md)
- [Updatable Implementations](./module/updatable-implementations.md)

## Relationships

### Inherited By
- [ALiBi](./alibi.md)
- [ArrayOffsetLayer](./arrayoffsetlayer.md)
- [BatchNorm](./batchnorm.md)
- [Bilinear](./bilinear.md)
- [CELU](./celu.md)
- [Conv1d](./conv1d.md)
- [Conv2d](./conv2d.md)
- [Conv3d](./conv3d.md)
- [ConvTransposed1d](./convtransposed1d.md)
- [ConvTransposed2d](./convtransposed2d.md)
- [ConvTransposed3d](./convtransposed3d.md)
- [Dropout](./dropout.md)
- [Dropout2d](./dropout2d.md)
- [Dropout3d](./dropout3d.md)
- [ELU](./elu.md)
- [Embedding](./embedding.md)
- [GELU](./gelu.md)
- [GLU](./glu.md)
- [GRU](./gru.md)
- [GroupNorm](./groupnorm.md)
- [HardShrink](./hardshrink.md)
- [HardSwish](./hardswish.md)
- [HardTanh](./hardtanh.md)
- [Identity](./identity.md)
- [InstanceNorm](./instancenorm.md)
- [LSTM](./lstm.md)
- [LayerNorm](./layernorm.md)
- [LeakyReLU](./leakyrelu.md)
- [Linear](./linear.md)
- [LogSigmoid](./logsigmoid.md)
- [LogSoftmax](./logsoftmax.md)
- [Mish](./mish.md)
- [MultiHeadAttention](./multiheadattention.md)
- [OffsetLayer](./offsetlayer.md)
- [PReLU](./prelu.md)
- [Pool](./pool.md)
- [Quantized](./quantized.md)
- [RMSNorm](./rmsnorm.md)
- [RNN](./rnn.md)
- [ReLU](./relu.md)
- [ReLU6](./relu6.md)
- [ReLUSquared](./relusquared.md)
- [RoPE](./rope.md)
- [SELU](./selu.md)
- [Sequential](./sequential.md)
- [SiLU](./silu.md)
- [Sigmoid](./sigmoid.md)
- [SinusoidalPositionalEncoding](./sinusoidalpositionalencoding.md)
- [Softmax](./softmax.md)
- [Softmin](./softmin.md)
- [Softplus](./softplus.md)
- [Softshrink](./softshrink.md)
- [Softsign](./softsign.md)
- [Step](./step.md)
- [Tanh](./tanh.md)
- [Transformer](./transformer.md)
- [UnaryLayer](./unarylayer.md)
- [Upsample](./upsample.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable

## See Also

### Base Classes and Interfaces
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
- [enum ModuleValue](./modulevalue.md)
  A single value from [`Module`](./module.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module)*