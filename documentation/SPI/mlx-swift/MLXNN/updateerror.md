---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/updateerror"
framework: "mlx-swift/MLXNN"
---

# UpdateError

**Framework**: mlx-swift/MLXNN  
**Kind**: enum  
**Role**: Enumeration

## Declaration

```swift
enum UpdateError
```

## Topics

### Enumeration Cases
- [case incompatibleItems(path: [String], modules: [String], item: String, value: String)](./updateerror/incompatibleitems%28path,modules,item,value%29.md)
- [case keyNotFound(path: [String], modules: [String])](./updateerror/keynotfound%28path,modules%29.md)
- [case mismatchedContainers(base: String, key: String)](./updateerror/mismatchedcontainers%28base,key%29.md)
- [case mismatchedSize(path: [String], modules: [String], expectedShape: [Int], actualShape: [Int])](./updateerror/mismatchedsize%28path,modules,expectedshape,actualshape%29.md)
- [UpdateError.needModuleInfo(_:)](./updateerror/needmoduleinfo%28_%29.md)
- [case settingArrayWithModule(path: [String], modules: [String])](./updateerror/settingarraywithmodule%28path,modules%29.md)
- [UpdateError.unableToCast(_:)](./updateerror/unabletocast%28_%29.md)
- [case unableToCollectModulesFromContainer(path: [String], modules: [String])](./updateerror/unabletocollectmodulesfromcontainer%28path,modules%29.md)
- [UpdateError.unableToSet(_:)](./updateerror/unabletoset%28_%29.md)
- [case unexpectedStructure(key: String, item: String)](./updateerror/unexpectedstructure%28key,item%29.md)
- [case unhandledKeys(path: [String], modules: [String], keys: [String])](./updateerror/unhandledkeys%28path,modules,keys%29.md)
### Default Implementations
- [Error Implementations](./updateerror/error-implementations.md)
- [LocalizedError Implementations](./updateerror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Copyable
- Swift.Error
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/updateerror)*