---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/lexicographicallyprecedes(_:by:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# lexicographicallyPrecedes(_:by:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.lexicographicallyPrecedes(_:by:)`.

## Declaration

```swift
func lexicographicallyPrecedes<OtherSequence>(_ other: OtherSequence, by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/lexicographicallyprecedes(_:by:))*