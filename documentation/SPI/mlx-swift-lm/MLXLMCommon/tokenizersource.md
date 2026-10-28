---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenizersource"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TokenizerSource

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Identifies where a tokenizer should be loaded from.

## Declaration

```swift
enum TokenizerSource
```

## Overview

Used by [`ModelConfiguration`](./modelconfiguration.md) to specify an alternate tokenizer source when the tokenizer files are not co-located with the model weights.

- [`TokenizerSource.id(_:revision:)`](./tokenizersource/id%28_,revision%29.md) downloads tokenizer files from a remote provider (requires a [`Downloader`](./downloader.md))
- [`TokenizerSource.directory(_:)`](./tokenizersource/directory%28_%29.md) loads tokenizer files from a local path

When `nil` on a [`ModelConfiguration`](./modelconfiguration.md), the tokenizer is loaded from the same directory as the model.

## Topics

### Enumeration Cases
- [TokenizerSource.directory(_:)](./tokenizersource/directory%28_%29.md)
  A local directory containing tokenizer files.
- [case id(String, revision: String?)](./tokenizersource/id%28_,revision%29.md)
  A provider-specific repository identifier for downloading tokenizer files.
### Default Implementations
- [Equatable Implementations](./tokenizersource/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenizersource)*