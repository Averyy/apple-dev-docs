---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftercontainer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPDrafterContainer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Sendable container for an [`MTPDrafterContext`](./mtpdraftercontext.md).

## Declaration

```swift
final class MTPDrafterContainer
```

#### Overview

Mirrors the [`ModelContainer`](./modelcontainer.md) pattern: a `final class : Sendable` that wraps the non-Sendable context in a `SerialAccessContainer` and exposes async `perform(_:)` closures for serialized access.

## Topics

### Initializers
- [init(context: consuming MTPDrafterContext)](./mtpdraftercontainer/init%28context%29.md)
### Instance Properties
- [var configuration: ModelConfiguration](./mtpdraftercontainer/configuration.md)
### Instance Methods
- [func perform<R>(@Sendable (MTPDrafterContext) async throws -> sending R) async rethrows -> sending R](./mtpdraftercontainer/perform%28_%29.md)
  Perform an action on the [`MTPDrafterContext`](./mtpdraftercontext.md). Callers *must* eval any `MLXArray` before returning as `MLXArray` is not `Sendable`.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftercontainer)*