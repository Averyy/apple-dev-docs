---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcomponentsproviding/modelcomponents"
framework: "mlx-swift-lm/MLXLMCommon"
---

# modelComponents

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The checkpoint components that make up each model component.

## Declaration

```swift
var modelComponents: [ModelComponent : [CheckpointComponent]] { get }
```

## Discussion

Each [`destination`](../checkpointcomponent/destination.md) is the path of an optional module. Its [`namespaces`](../checkpointcomponent/namespaces.md) list every serialized prefix of the module’s tensors, as they appear before [`prepareCheckpoint(_:)`](../baselanguagemodel/preparecheckpoint%28_%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcomponentsproviding/modelcomponents)*