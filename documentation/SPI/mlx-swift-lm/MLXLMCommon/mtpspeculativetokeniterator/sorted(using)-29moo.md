---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpspeculativetokeniterator/sorted(using:)-29moo"
framework: "mlx-swift-lm/MLXLMCommon"
---

# sorted(using:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.sorted(using:)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
func sorted<S, Comparator>(using comparators: S) -> [Self.Element] where S : Sequence, Comparator : SortComparator, Comparator == S.Element, Self.Element == Comparator.Compared
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpspeculativetokeniterator/sorted(using:)-29moo)*