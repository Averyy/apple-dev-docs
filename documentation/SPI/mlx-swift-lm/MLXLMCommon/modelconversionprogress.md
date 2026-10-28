---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionprogress"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionProgress

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Progress update emitted by the Swift conversion pipeline.

## Declaration

```swift
struct ModelConversionProgress
```

## Overview

This intentionally stays coarse-grained so applications can map it onto their own UI without inheriting implementation details. Download progress is forwarded as a fractional value when the downloader provides one.

## Topics

### Initializers
- [init(stage: ModelConversionStage, fractionCompleted: Double?, message: String?)](./modelconversionprogress/init%28stage,fractioncompleted,message%29.md)
### Instance Properties
- [let fractionCompleted: Double?](./modelconversionprogress/fractioncompleted.md)
- [let message: String?](./modelconversionprogress/message.md)
- [let stage: ModelConversionStage](./modelconversionprogress/stage.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionprogress)*