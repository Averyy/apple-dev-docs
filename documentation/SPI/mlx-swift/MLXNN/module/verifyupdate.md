---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/verifyupdate"
framework: "mlx-swift/MLXNN"
---

# Module.VerifyUpdate

**Framework**: mlx-swift/MLXNN  
**Kind**: struct  
**Role**: Structure

Options for verifying [`update(parameters:verify:path:modulePath:)`](./update%28parameters,verify,path,modulepath%29.md) and [`update(modules:verify:path:modulePath:)`](./update%28modules,verify,path,modulepath%29.md).

## Declaration

```swift
struct VerifyUpdate
```

## Topics

### Initializers
- [init(rawValue: Int)](./verifyupdate/init%28rawvalue%29.md)
### Instance Properties
- [let rawValue: Int](./verifyupdate/rawvalue.md)
### Type Properties
- [static let all: Module.VerifyUpdate](./verifyupdate/all.md)
- [static let allModelKeysSet: Module.VerifyUpdate](./verifyupdate/allmodelkeysset.md)
- [static let noUnusedKeys: Module.VerifyUpdate](./verifyupdate/nounusedkeys.md)
  Check that all keys are used.  This is useful to ensure that e.g. all loaded parameters are used – there are no names that don’t match.
- [static let none: Module.VerifyUpdate](./verifyupdate/none.md)
- [static let shapeMismatch: Module.VerifyUpdate](./verifyupdate/shapemismatch.md)
### Default Implementations
- [Equatable Implementations](./verifyupdate/equatable-implementations.md)
- [OptionSet Implementations](./verifyupdate/optionset-implementations.md)
- [SetAlgebra Implementations](./verifyupdate/setalgebra-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.ExpressibleByArrayLiteral
- Swift.OptionSet
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype
- Swift.SetAlgebra


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/verifyupdate)*