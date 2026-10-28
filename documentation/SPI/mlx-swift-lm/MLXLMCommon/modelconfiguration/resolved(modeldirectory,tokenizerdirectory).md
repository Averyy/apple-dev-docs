---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/resolved(modeldirectory:tokenizerdirectory:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# resolved(modelDirectory:tokenizerDirectory:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Maps this configuration’s behavioral properties into a [`ResolvedModelConfiguration`](../resolvedmodelconfiguration.md) with the given directories.

## Declaration

```swift
func resolved(modelDirectory: URL, tokenizerDirectory: URL) -> ResolvedModelConfiguration
```

## Discussion

This is a pure data mapping with no I/O. The directories should already be resolved (downloaded or local) before calling this method.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/resolved(modeldirectory:tokenizerdirectory:))*