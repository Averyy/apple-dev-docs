---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/withserialexecutor(_:)-7m5d8"
framework: "mlx-swift-lm/MLXLMCommon"
---

# withSerialExecutor(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Inherited from `Actor.withSerialExecutor(_:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func withSerialExecutor<T, E>(_ operation: (any SerialExecutor) throws(E) -> T) throws(E) -> T where E : Error, T : ~Copyable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/withserialexecutor(_:)-7m5d8)*