---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/flatmap(_:)-6878x"
framework: "mlx-swift-lm/MLXLMCommon"
---

# flatMap(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.flatMap(_:)`.

**Availability**:
- Swift - Deprecated in 4.1 (renamed: compactMap(_:))

> **Deprecated**: Please use compactMap(_:) for the case where closure returns an optional value

## Declaration

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/flatmap(_:)-6878x)*