---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/assumeisolated(_:file:line:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# assumeIsolated(_:file:line:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Inherited from `Actor.assumeIsolated(_:file:line:)`.

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
func assumeIsolated<T>(_ operation: (isolated Self) throws -> T, file: StaticString = #fileID, line: UInt = #line) rethrows -> T where T : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/assumeisolated(_:file:line:))*