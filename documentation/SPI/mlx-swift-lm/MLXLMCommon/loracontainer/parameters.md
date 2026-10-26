---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/parameters"
framework: "mlx-swift-lm/MLXLMCommon"
---

# parameters

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

The parameter values for the adapter modules.

## Declaration

```swift
let parameters: ModuleParameters
```

#### Discussion

> ❗ **Important**: This contains MLXArray which is not Sendable, but in this case we ensure that they are fully evaluated and never updated.  These static MLXArrays are usable across threads but we cannot prove so to the type checker so this is left as `@unchecked Sendable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/parameters)*