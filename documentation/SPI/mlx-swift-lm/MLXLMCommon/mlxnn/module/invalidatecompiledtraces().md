---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mlxnn/module/invalidatecompiledtraces()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# invalidateCompiledTraces()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Drops every compiled trace stored in this module tree.

## Declaration

```swift
func invalidateCompiledTraces()
```

#### Discussion

A [`CompiledTrace`](../../compiledtrace.md) is built from the modules present when it first ran, so anything that replaces modules leaves it stale: loading, fusing, or unloading an adapter, quantizing a loaded model. Weight updates that keep the tree intact, such as training steps, do not need this. Traces are found by reflection, so storing one is all a module has to do: there is no conformance to remember.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mlxnn/module/invalidatecompiledtraces())*