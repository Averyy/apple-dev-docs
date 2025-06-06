# categoryOrder

**Framework**: Accessibility  
**Kind**: property

A list of every category value for the axis in the order they appear visually in the graph or legend.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var categoryOrder: [String] { get set }
```

#### Discussion

If your categorical axis represents, for example, blood type data, and the legend lists , , ,  in that order, provide an array that contains the strings `"AB"`, `"A"`, `"B"`, and `"O"` in the same order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axcategoricaldataaxisdescriptor/categoryorder)*