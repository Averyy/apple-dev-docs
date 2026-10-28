---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftercontext"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPDrafterContext

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Lightweight context for an MTP drafter — simpler than `ModelContext` because drafters have no tokenizer, no user input processor, no chat template.

## Declaration

```swift
struct MTPDrafterContext
```

## Overview

Not `Sendable`; cross-domain access goes through [`MTPDrafterContainer`](./mtpdraftercontainer.md).

## Topics

### Initializers
- [init(configuration: ModelConfiguration, model: any MTPDrafterModel)](./mtpdraftercontext/init%28configuration,model%29.md)
### Instance Properties
- [var configuration: ModelConfiguration](./mtpdraftercontext/configuration.md)
- [var model: any MTPDrafterModel](./mtpdraftercontext/model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftercontext)*