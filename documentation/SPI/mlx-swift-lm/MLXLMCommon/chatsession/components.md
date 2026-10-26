---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/components"
framework: "mlx-swift-lm/MLXLMCommon"
---

# components

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Optional behavioral components (e.g. a custom [`LogitProcessor`](../logitprocessor.md)) applied on each generation. The `logitProcessorFactory` is invoked fresh for every [`respond(to:role:images:videos:audios:)`](./respond%28to,role,images,videos,audios%29.md) so stateful processors do not leak state across turns.

## Declaration

```swift
var components: GenerationComponents
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/components)*