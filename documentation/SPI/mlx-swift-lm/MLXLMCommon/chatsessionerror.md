---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsessionerror"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ChatSessionError

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Errors thrown by [`ChatSession`](./chatsession.md).

## Declaration

```swift
enum ChatSessionError
```

## Topics

### Enumeration Cases
- [ChatSessionError.emptyPreparedInput](./chatsessionerror/emptypreparedinput.md)
  The processor produced no tokens for generation.
- [case kvCacheConfigurationChanged(previous: KVCacheConfiguration?, requested: KVCacheConfiguration?)](./chatsessionerror/kvcacheconfigurationchanged%28previous,requested%29.md)
  The cache was realized under a different KV-cache configuration.
- [ChatSessionError.noCacheAvailable](./chatsessionerror/nocacheavailable.md)
  [`saveCache(to:)`](./chatsession/savecache%28to%29.md) was called before any generation occurred.
### Instance Properties
- [var errorDescription: String?](./chatsessionerror/errordescription.md)
### Default Implementations
- [Error Implementations](./chatsessionerror/error-implementations.md)
- [LocalizedError Implementations](./chatsessionerror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsessionerror)*