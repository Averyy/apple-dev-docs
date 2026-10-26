---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager/withserialexecutor(_:)-65wll"
framework: "mlx-swift/MLX"
---

# withSerialExecutor(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Inherited from `Actor.withSerialExecutor(_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func withSerialExecutor<T, E>(_ operation: nonisolated(nonsending) (any SerialExecutor) async throws(E) -> T) async throws(E) -> T where E : Error, T : ~Copyable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager/withserialexecutor(_:)-65wll)*