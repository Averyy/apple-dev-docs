---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/updatemissing(parameter:verify:path:modulepath:)"
framework: "mlx-swift/MLXNN"
---

# updateMissing(parameter:verify:path:modulePath:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Called from [`update(parameters:verify:path:modulePath:)`](./update%28parameters,verify,path,modulepath%29.md) if a required parameter is missing.

## Declaration

```swift
func updateMissing(parameter: String, verify: Module.VerifyUpdate, path: [String], modulePath: [String]) throws
```

## Discussion

The default implementation will throw [`UpdateError.keyNotFound(path:modules:)`](../updateerror/keynotfound%28path,modules%29.md).

## Parameters

- `parameter`: The key for the missing parameter
- `verify`: Verify settings
- `path`: Path to the key (includes parameter)
- `modulePath`: Path to the module


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/updatemissing(parameter:verify:path:modulepath:))*