---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/downloader"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Downloader

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A protocol for downloading model repository snapshots to local directories.

## Declaration

```swift
protocol Downloader : Sendable
```

## Mentions

- [Using mlx-swift-lm](./using.md)

## Overview

Conforming types encapsulate the full download lifecycle — cache check, network download, and fallback to cache on failure. Each conformance owns its own caching strategy. The return value is always a local directory URL containing the requested files.

The protocol is provider-agnostic. `id` is a plain `String` that each conformance interprets however it wants (e.g. `"org/model"` for Hugging Face, a four-part Kaggle handle, an S3 path). `revision` is optional for providers without versioning.

## Topics

### Instance Methods
- [func download(id: String, revision: String?, matching: [String], useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> URL](./downloader/download%28id,revision,matching,uselatest,progresshandler%29.md)
  Download (or retrieve from cache) a snapshot of a repository.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Related Documentation
- [struct ResolvedModelConfiguration](./resolvedmodelconfiguration.md)
  A fully resolved model configuration where all sources have been resolved to local directory paths.
- [enum TokenizerSource](./tokenizersource.md)
  Identifies where a tokenizer should be loaded from.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/downloader)*