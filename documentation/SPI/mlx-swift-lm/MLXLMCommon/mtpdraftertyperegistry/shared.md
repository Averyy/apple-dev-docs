---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftertyperegistry/shared"
framework: "mlx-swift-lm/MLXLMCommon"
---

# shared

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Type Property

Shared registry. Empty until a downstream module registers a drafter type via `await MTPDrafterTypeRegistry.shared.registerModelType(...)`.

## Declaration

```swift
static let shared: ModelTypeRegistry<any MTPDrafterModel>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftertyperegistry/shared)*