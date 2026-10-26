---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/componentloading/onfirstuse"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ComponentLoading.onFirstUse

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Load each of [`onDemandComponents`](../modelcomponentsproviding/ondemandcomponents.md) the first time an input needs it, the way an `MLXArray` is computed only when it is evaluated. The checkpoint files must stay readable until then.

## Declaration

```swift
case onFirstUse
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/componentloading/onfirstuse)*